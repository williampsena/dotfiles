#!/usr/bin/env bash
dir="$(pwd)"
base_dir=$(realpath "$(pwd)/..")

source $base_dir/_settings.sh

change_wallpaper=$(get_yaml_value ".commands.change_wallpaper")

options="Open Terminal\nChange Wallpaper\nRestart Qtile\nShutdown"

chosen=$(echo -e "$options" | rofi  -dmenu -p "Menu")

# Take action based on the selected option
case "$chosen" in
    "Open Terminal")
        kitty &
        ;;
    "Restart Qtile")
        qtile cmd-obj -o cmd -f restart
        ;;
    "Change Wallpaper")
        # TODO load from yaml
        $HOME/.config/qtile/ebenezer/scripts/wallpaper.sh set ~/Pictures/Wallpapers/Active/
        ;;
    "Shutdown")
        poweroff
        ;;
esac
