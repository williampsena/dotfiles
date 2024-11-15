#!/bin/bash

VM_NAME="ArchLinuxVM"
VM_FOLDER="$HOME/VirtualBox VMs"
VM_HOME="$(pwd)/.vm"
VDI_BASE_PATH="$VM_HOME/arch-linux-base.vdi"
VDI_PATH="$(pwd)/.vm/arch-linux.vdi"
VM_PASSWORD="osboxes.org"
RDP_PORT="10001"
SSH_PORT="2222"
SSH_USER="osboxes"
VM_IP="127.0.0.1"

option=$1

download_iso() {
    local iso_path="$VM_HOME/arch_64bit.7z"
    if [[ ! -f "$iso_path" ]]; then
        echo "Downloading Arch Linux ISO..."
        wget -O "$iso_path" "https://sourceforge.net/projects/osboxes/files/v/vb/4-Ar---c-x/20240601/CLI/64bit.7z/download"
    else
        echo "The Arch Linux ISO is already downloaded."
    fi

    if [[ ! -f "$VDI_BASE_PATH" ]]; then
        echo "Extracting Arch Linux VDI..."
        7z x "$iso_path" -o"$VM_HOME"
        mv "$VM_HOME/Arch-Linux-x86_64.vdi" "$VDI_BASE_PATH"
    else
        echo "The Arch Linux VDI is already extracted."
    fi
}

create_vm() {
    if [[ ! -f "$VDI_PATH" ]]; then
        echo "😮 VDI not found. Copying base VDI..."
        cp "$VDI_BASE_PATH" "$VDI_PATH"
    fi

    if ! VBoxManage list vms | grep -q "\"$VM_NAME\""; then
        echo "🚧 Creating VM..."
        VBoxManage createvm --name "$VM_NAME" --register --basefolder "$VM_FOLDER" --ostype "Linux_64"
    else
        echo "💖 VM already exists."
    fi

    echo "🖥️ Configuring VM settings (CPU, RAM, Network)..."
    VBoxManage modifyvm "$VM_NAME" --ioapic on
    VBoxManage modifyvm "$VM_NAME" --cpus 2 --memory 6144 --vram 128
    VBoxManage modifyvm "$VM_NAME" --nic1 nat
    VBoxManage modifyvm "$VM_NAME" --graphicscontroller vmsvga
    VBoxManage modifyvm "$VM_NAME" --accelerate3d on

    echo "⛃ Configuring storage..."
    VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAhci
    VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$VDI_PATH"
    VBoxManage modifyvm "$VM_NAME" --boot1 disk

    echo "🔗 Configuring RDP..."
    VBoxManage modifyvm "$VM_NAME" --vrde on
    VBoxManage modifyvm "$VM_NAME" --vrdemulticon on --vrdeport "$RDP_PORT"
    VBoxManage modifyvm "$VM_NAME" --natpf1 "ssh,tcp,,${SSH_PORT},,22"

    start_vm

    echo "🫠 Waiting for SSH access..."

    while ! ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "$SSH_USER@$VM_IP" -p "$SSH_PORT" "exit"; do
        echo "Waiting for SSH access..."
        sleep 5
    done

    echo "🔥 VM is up and SSH is available."

    # Disabled temporary SSH connection has stopped working.
    # install_guest_additions
}

install_guest_additions() {
    echo "📦 Installing VirtualBox Guest Additions..."

    local iso_path="$VM_HOME/additions.iso"

    if [[ ! -f "$iso_path" ]]; then
        echo "Downloading Virtual Box Guest Additions ISO..."
        wget https://download.virtualbox.org/virtualbox/7.1.0/VBoxGuestAdditions_7.1.0.iso -O $iso_path
    else
        echo "The Downloading Virtual Box Guest Additions is already downloaded."
    fi

    VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium $iso_path

    echo "✅ Guest Additions installed."
}

umount_guest_additions() {
    VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium none
}

start_vm() {
    VM_STATUS=$(VBoxManage list runningvms | grep "\"$VM_NAME\"")

    if [[ -z "$VM_STATUS" ]]; then
        echo "🏁 Starting VM..."
        VBoxHeadless --startvm "$VM_NAME" &>/dev/null &
        sleep 60
    else
        echo "🖥️ VM is already running."
    fi
}

stop_vm() {
    VM_STATUS=$(VBoxManage list runningvms | grep "\"$VM_NAME\"")

    if [[ -n "$VM_STATUS" ]]; then
        echo "🛑 Stopping VM..."
        VBoxManage controlvm "$VM_NAME" acpipowerbutton
        sleep 10
        if VBoxManage list runningvms | grep -q "\"$VM_NAME\""; then
            echo "⚠️ VM did not shut down gracefully, forcing power off..."
            VBoxManage controlvm "$VM_NAME" poweroff
        fi
    else
        echo "🖥️ VM is not running."
    fi
}

connect_ssh() {
    echo "🌐 Connecting over ssh..."

    sync
    sshpass -p "$VM_PASSWORD" ssh "$SSH_USER@$VM_IP" -p "$SSH_PORT"
}

sync() {
    sshpass -p "$VM_PASSWORD" scp -P "$SSH_PORT" _install_arch.sh "$SSH_USER@$VM_IP:/tmp/install.sh"
}

case $option in
download_iso)
    download_iso
    ;;
create)
    create_vm
    ;;
install_guest_additions)
    install_guest_additions
    ;;
umount_guest_additions)
    umount_guest_additions
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
    echo "Usage: $0 {create|download_iso|install_guest_additions|start|ssh|sync|umount_guest_additions}"
    exit 1
    ;;
esac
