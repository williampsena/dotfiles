# About

This repository includes my dot files and python scripts for Qtile.

This theme was named *Ebenezer* 🪨, which meaning "stone of helper.".

>> The quote is from I Samuel 7. After defeating the Philistines, Samuel raises his *Ebenezer*, declaring that God defeated the enemies on this spot. As a result, "hither by thy help I come."  So I hope this stone helps you in your environment and, more importantly, in your life. 🙏🏿

🚜👷🚧🏗️ This setup is under building; I'm switching my dotfiles inspired setup from Awesome Lua to Python.

# Installing

```shell
pamac install dunst ttf-dejavu brightnessctl arc-gtk-theme ttf-firacode-nerd ttf-hack-nerd unclutter nerd-fonts-inter ttf-fira-sans python-pyaml python-pulsectl-asyncio python-dbus-next python-psutil python-pytest-subtests python-pulsectl-asyncio pulsemixer papirus-icon-theme pavucontrol xautolock scrot i3lock flameshot feh lxsession network-manager-applet nm-connection-editor nm-applet picom-git yq

DOTFILES_PATH="$HOME/dotfiles"
mkdir -p $DOTFILES_PATH

ln -sf $DOTFILES_PATH/qtile $HOME/.config/qtile  
ln -sf $DOTFILES_PATH/dunst $HOME/.config/dunst  
```

# Inspirations

- https://github.com/JhonatanFerrer/JhoalfercoQtileDotfiles
- https://gitlab.com/dwt1/dotfiles
- https://github.com/neo-fetch/shinrai-dotfiles
- https://github.com/adi1090x/rofi?tab=readme-ov-file
- https://github.com/SapuSeven/rofi-presets