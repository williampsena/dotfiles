#!/bin/bash

# General VM Configuration
VM_FOLDER="$HOME/VirtualBox VMs"
VM_HOME="$(pwd)/.vm"
RDP_PORT_ARCH="10001"
RDP_PORT_DEBIAN="10002"
SSH_PORT_ARCH="2222"
SSH_PORT_DEBIAN="2223"
VM_IP="127.0.0.1"

SSH_USER="osboxes"
VM_PASSWORD="osboxes.org"

# Arch Linux VM Configuration
ARCH_VM_NAME="ArchLinuxVM"
ARCH_VDI_BASE_PATH="$VM_HOME/arch-linux-base.vdi"
ARCH_VDI_PATH="$VM_HOME/arch-linux.vdi"
ARCH_ISO_URL="https://sourceforge.net/projects/osboxes/files/v/vb/4-Ar---c-x/20240601/CLI/64bit.7z/download"

# Debian VM Configuration
DEBIAN_VM_NAME="DebianVM"
DEBIAN_VDI_BASE_PATH="$VM_HOME/debian-base.vdi"
DEBIAN_VDI_PATH="$VM_HOME/debian.vdi"
DEBIAN_ISO_URL="https://sourceforge.net/projects/osboxes/files/v/vb/14-D-b/12.6.0/64bit.7z/download"

option=$1
vm_type=$2 # Specify "arch" or "debian"

get_vm_name() {
    if [[ "$vm_type" == "arch" ]]; then
        echo "$ARCH_VM_NAME"
    elif [[ "$vm_type" == "debian" ]]; then
        echo "$DEBIAN_VM_NAME"
    else
        echo "Invalid VM type. Use 'arch' or 'debian'." >&2
        exit 1
    fi
}

get_vm_ssh_port() {
    if [[ "$vm_type" == "arch" ]]; then
        echo "$SSH_PORT_ARCH"
    elif [[ "$vm_type" == "debian" ]]; then
        echo "$SSH_PORT_DEBIAN"
    else
        echo "Invalid VM type. Use 'arch' or 'debian'." >&2
        exit 1
    fi
}

download_iso() {
    local iso_path
    local iso_url

    if [[ "$vm_type" == "arch" ]]; then
        iso_path="$VM_HOME/arch_64bit.7z"
        iso_url="$ARCH_ISO_URL"
    elif [[ "$vm_type" == "debian" ]]; then
        iso_path="$VM_HOME/debian_64bit.7z"
        iso_url="$DEBIAN_ISO_URL"
    else
        echo "Invalid VM type. Use 'arch' or 'debian'."
        exit 1
    fi

    if [[ ! -f "$iso_path" ]]; then
        echo "Downloading $vm_type ISO..."
        wget -O "$iso_path" "$iso_url"
    else
        echo "The $vm_type ISO is already downloaded."
    fi

    if [[ "$vm_type" == "arch" && ! -f "$ARCH_VDI_BASE_PATH" ]]; then
        echo "Extracting Arch Linux VDI..."
        7z x "$iso_path" -o"$VM_HOME"
        mv "$VM_HOME/Arch-Linux-x86_64.vdi" "$ARCH_VDI_BASE_PATH"
    elif [[ "$vm_type" == "debian" && ! -f "$DEBIAN_VDI_BASE_PATH" ]]; then
        echo "Extracting Debian VDI..."
        7z x "$iso_path" -o"$VM_HOME"
        mv "$VM_HOME/64bit/Debian 12.6.0 (64bit).vdi" "$DEBIAN_VDI_BASE_PATH"
    else
        echo "The $vm_type VDI is already extracted."
    fi
}

create_vm() {
    local vm_name
    local vdi_path
    local vdi_base_path
    local rdp_port
    local ssh_port

    if [[ "$vm_type" == "arch" ]]; then
        vm_name="$ARCH_VM_NAME"
        vdi_path="$ARCH_VDI_PATH"
        vdi_base_path="$ARCH_VDI_BASE_PATH"
        rdp_port="$RDP_PORT_ARCH"
        ssh_port="$SSH_PORT_ARCH"
    elif [[ "$vm_type" == "debian" ]]; then
        vm_name="$DEBIAN_VM_NAME"
        vdi_path="$DEBIAN_VDI_PATH"
        vdi_base_path="$DEBIAN_VDI_BASE_PATH"
        rdp_port="$RDP_PORT_DEBIAN"
        ssh_port="$SSH_PORT_DEBIAN"
    else
        echo "Invalid VM type. Use 'arch' or 'debian'."
        exit 1
    fi

    if [[ ! -f "$vdi_path" ]]; then
        echo "😮 VDI $vdi_path not found. Copying base VDI..."
        cp "$vdi_base_path" "$vdi_path"
    fi

    if ! VBoxManage list vms | grep -q "\"$vm_name\""; then
        echo "🚧 Creating $vm_type VM..."
        VBoxManage createvm --name "$vm_name" --register --basefolder "$VM_FOLDER" --ostype "Linux_64"
    else
        echo "💖 $vm_type VM already exists."
    fi

    echo "🖥️  Configuring $vm_type VM settings (CPU, RAM, Network)..."
    VBoxManage modifyvm "$vm_name" --ioapic on
    VBoxManage modifyvm "$vm_name" --cpus 2 --memory 6144 --vram 128
    VBoxManage modifyvm "$vm_name" --nic1 nat
    VBoxManage modifyvm "$vm_name" --graphicscontroller vmsvga
    VBoxManage modifyvm "$vm_name" --accelerate3d on

    echo "⛃ Configuring storage..."
    VBoxManage storagectl "$vm_name" --name "SATA Controller" --add sata --controller IntelAhci
    VBoxManage storageattach "$vm_name" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$vdi_path"
    VBoxManage modifyvm "$vm_name" --boot1 disk

    echo "🔗 Configuring RDP..."
    VBoxManage modifyvm "$vm_name" --vrde on
    VBoxManage modifyvm "$vm_name" --vrdemulticon on --vrdeport "$rdp_port"
    VBoxManage modifyvm "$vm_name" --natpf1 "ssh,tcp,,${ssh_port},,22"

    start_vm
}

start_vm() {
    local vm_name=$(get_vm_name)

    VM_STATUS=$(VBoxManage list runningvms | grep "\"$vm_name\"")

    if [[ -z "$VM_STATUS" ]]; then
        echo "🏁 Starting $vm_type VM..."
        VBoxHeadless --startvm "$vm_name" &>/dev/null &
        sleep 60
    else
        echo "🖥️ $vm_type VM is already running."
    fi
}

stop_vm() {
    local vm_name = $(get_vm_name)

    VM_STATUS=$(VBoxManage list runningvms | grep "\"$vm_name\"")

    if [[ -n "$VM_STATUS" ]]; then
        echo "🛑 Stopping $vm_type VM..."
        VBoxManage controlvm "$vm_name" acpipowerbutton
        sleep 10
        if VBoxManage list runningvms | grep -q "\"$vm_name\""; then
            echo "⚠️ $vm_type VM did not shut down gracefully, forcing power off..."
            VBoxManage controlvm "$vm_name" poweroff
        fi
    else
        echo "🖥️ $vm_type VM is not running."
    fi
}

connect_ssh() {
    echo "🌐 Connecting over ssh..."

    local ssh_port=$(get_vm_ssh_port)

    sync
    sshpass -p "$VM_PASSWORD" ssh "$SSH_USER@$VM_IP" -p "$ssh_port"
}

sync() {
    local ssh_port=$(get_vm_ssh_port)
    sshpass -p "$VM_PASSWORD" scp -P "$ssh_port" _install_debian.sh "$SSH_USER@$VM_IP:/tmp/install.sh"
}

case $option in
download_iso)
    download_iso
    ;;
create)
    create_vm
    ;;
start)
    start_vm
    ;;
stop)
    stop_vm
    ;;
ssh)
    connect_ssh
    ;;
sync)
    sync
    ;;
*)
    echo "Usage: $0 {download_iso|create|start|stop|ssh|sync} {arch|debian}"
    exit 1
    ;;
esac
