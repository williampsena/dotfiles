#!/bin/bash

set -e

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "😎 Please run as root"
        exit 1
    fi
}

install_packages() {
    apt update && apt upgrade -y

    local packages="alacritty firefox-esr lm-sensors x11vnc dbus-x11 \
        notification-daemon xorg xserver-xorg xinit git build-essential dunst fonts-dejavu \
        fonts-firacode fonts-hack-ttf fonts-jetbrains-mono unclutter \
        fonts-firacode fonts-mononoki pulsemixer papirus-icon-theme pavucontrol xautolock \
        xss-lock scrot i3lock flameshot feh lxsession network-manager-gnome python3-requests \
        python3 python3-pip python3-pillow python3-psutil python3-dbus pipenv python3.11-venv rofi \
        pcmanfm-qt passwd xserver-xorg xinit libpangocairo-1.0-0 python3-pip python3-xcffib python3-cairocffi xcb xcb-proto picom"

    apt install -y $packages
}

install_qtile() {
    mkdir -p /opt/python-envs
    python3 -m venv /opt/python-envs/qtile
    /opt/python-envs/qtile/bin/pip3 install qtile qtile-ebenezer
    ln -f /opt/python-envs/qtile/bin/qtile /usr/bin/qtile

    cat <<EOF > /usr/share/xsessions/qtile.desktop
[Desktop Entry]
Version=1.0
Name=Qtile
Comment=Dynamic tiling window manager
Exec=env PATH=\$PATH:/opt/python-envs /opt/python-envs/qtile/bin/qtile start
TryExec=qtile
Icon=
Type=Application
X-LightDM-DesktopName=Qtile
EOF


}

install_extra_packages() {
    echo "Installing additional packages not available in APT..."

    # Nerd Fonts
    if ! fc-list | grep -q "Nerd Font"; then
        echo "Installing Nerd Fonts..."
        mkdir -p /usr/share/fonts/nerd-fonts

        fonts=("FiraCode" "Iosevka")
        base_url="https://github.com/ryanoasis/nerd-fonts/releases/latest/download"

        for font in "${fonts[@]}"; do
            wget -qO "/tmp/${font}.zip" "${base_url}/${font}.zip"
            unzip -o "/tmp/${font}.zip" -d /usr/share/fonts/nerd-fonts
        done

        fc-cache -fv
    fi
}

setup_dotfiles() {
    local dotfiles="alacritty dunst flameshot fontconfig gtk-3.0 gtk-4.0 i3lock lxqt pcmanfm picom qt5ct qt6ct qtile rofi vscode xrandr .gtkrc-2.0"

    mkdir -p $HOME/.config

    for dotfile in $dotfiles; do
        src="$DOTFILES/$dotfile"
        dest="$HOME/.config/$dotfile"

        if [ -d "$src" ]; then
            mkdir -p $dest
            cp -R "$src" $HOME/.config
        else
            cp "$src" "$dest"
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
}

setup_qtile() {
    echo "🚀 Setting up qtile desktop"

    sudo -u qtileuser bash <<EOF
mkdir -p /home/qtileuser
cd /home/qtileuser

if [ -d "/home/qtileuser/dotfiles" ]; then
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

post_install() {
    echo "Enabling graphical target and services..."
    systemctl set-default graphical.target
    systemctl enable gdm
    systemctl start gdm

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
    install_extra_packages
    install_qtile
    setup_qtile
    post_install
    ;;
*)
    echo "Usage: $0 {install|setup-qtileuser}"
    exit 1
    ;;
esac

echo "🔥 Done"
