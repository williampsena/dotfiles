#!/bin/bash

set -e

setup_virtualbox_guest_additions() {
    mount /dev/cdrom /mnt
    /mnt/VBoxLinuxAdditions.run || true
    umount /mnt
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "😎 Please run as root"
        exit 1
    fi
}

install_packages() {
    [ -f /var/lib/pacman/db.lck ] && rm /var/lib/pacman/db.lck

    local packages="alacritty archlinux-wallpaper firefox lm_sensors qtile x11vnc dbus linux-headers xorg-server xorg-xinit xorg-server-xvfb xorg-twm xorg-xdm xorg-xclock xterm git base-devel dunst ttf-dejavu ttf-iosevka-nerd brightnessctl arc-gtk-theme ttf-firacode-nerd ttf-hack-nerd ttf-jetbrains-mono-nerd unclutter ttf-fira-sans ttf-mononoki-nerd pulsemixer papirus-icon-theme pavucontrol xautolock scrot i3lock flameshot feh lxsession network-manager-applet nm-connection-editor yq tk polkit-gnome qt5ct qt6ct network-manager-applet python-requests python python-pip python-pipenv python-pillow python-psutil python-requests python-pyaml python-dbus-next rofi"

    pacman -Syu --noconfirm &&
        pacman -S --needed --noconfirm $packages &&
        pacman -Scc --noconfirm
}

install_aur_packages() {
    local aur_packages="nerd-fonts-inter python-pulsectl-asyncio picom-git pamac-classic"

    sudo -u qtileuser bash <<EOF
    if ! command -v yay > /dev/null 2>&1; then
        git clone https://aur.archlinux.org/yay.git /tmp/yay &&
        cd /tmp/yay &&
        makepkg -si --noconfirm &&
        cd .. &&
        rm -rf /tmp/yay
    fi

    # Install AUR packages using yay
    yay -S --needed --noconfirm $aur_packages
EOF
}

setup_dotfiles() {
    local dotfiles="alacritty dunst flameshot fontconfig gtk-3.0 gtk-4.0 i3lock lxqt pcmanfm picom qt5ct qt6ct qtile rofi vscode xrandr .gtkr"

    mkdir -p $HOME/.config

    for dotfile in $dotfiles; do
        src="$DOTFILES/$dotfile"
        dest="$HOME/.config/$dotfile"

        mkdir -p $dest

        if [ -d "$src" ]; then
            cp -R "$src" $HOME/.config || true
        else
            cp "$src" $HOME/.config || true
        fi
    done
}

copy_files() {
    local files=(
        "qtile/colors.default.yml $HOME/.config/qtile/colors.yml"
        "qtile/applications.default.yml $HOME/.config/qtile/applications.yml"
        "qtile/config.default.yml $HOME/.config/qtile/config.yml"
    )

    for pair in "${files[@]}"; do
        src="$DOTFILES/$(echo $pair | awk '{print $1}')"
        dest=$(echo $pair | awk '{print $2}')

        if [ -f "$src" ]; then
            cp "$src" "$dest"
        else
            echo "👉 Source file $src does not exist. Skipping..."
        fi
    done
}

create_qtile_user() {
    useradd -m -s /bin/bash qtileuser || echo "User qtileuser already exists"

    echo 'qtileuser ALL=(ALL) NOPASSWD: ALL' >/etc/sudoers.d/qtileuser

    echo "qtileuser:qtile" | chpasswd

    echo "🔐 You must change password for 'qtileuser' manually for security reasons."

    sudo -u qtileuser bash <<EOF
    echo "exec qtile start" > /home/qtileuser/.xinitrc
    echo "exec qtile start" > ~/.xsession
    chmod +x ~/.xsession
EOF

    echo "needs_root_rights = no" >/etc/X11/Xwrapper.config
}

setup_qtile() {
    echo "🚀 Setting up qtile desktop"

    sudo -u qtileuser bash <<EOF
mkdir -p /home/qtileuser
cd /home/qtileuser

if [ -d "dotfiles" ] && [ "$(ls -A dotfiles)" ]; then
    echo "dotfiles directory already exists and is not empty. Skipping clone."
    (cd /home/qtileuser/dotfiles && git pull)
else
    git clone https://github.com/williampsena/dotfiles
fi

export DOTFILES=/home/qtileuser/dotfiles

bash /tmp/install.sh setup-qtileuser

(cd \$DOTFILES/qtile && make install)
EOF
}

disable_lockout() {
    echo "Disabling account lockout for multiple failed login attempts"

    cp /etc/pam.d/system-auth /etc/pam.d/system-auth.bak

    sed -i '/pam_faillock.so/s/^/#/' /etc/pam.d/system-auth

    echo "Account lockout disabled"
}

post_install() {
    # Disabled temporary SSH connection has stopped working.
    # setup_virtualbox_guest_additions
    disable_lockout

    systemctl enable xdm
    systemctl start xdm
    systemctl set-default graphical.target

    if ! systemctl is-enabled dbus.socket >/dev/null 2>&1; then
        systemctl enable dbus.socket
    fi

    systemctl start dbus.socket

    read -p "Reboot the system now? (y/n): " REBOOT
    if [[ "$REBOOT" =~ ^[Yy]$ ]]; then
        echo "Rebooting the system..."
        reboot
    else
        echo "Reboot skipped. Please reboot the system manually to apply changes."
    fi
}

option=${1:-install}

case $option in
setup-qtileuser)
    setup_dotfiles
    copy_files
    ;;
install)
    check_root
    create_qtile_user
    install_packages
    install_aur_packages
    setup_qtile
    post_install
    ;;
*)
    echo "Usage: $0 {install|setup-qtileuser}"
    exit 1
    ;;
esac

echo "🔥 Done"
