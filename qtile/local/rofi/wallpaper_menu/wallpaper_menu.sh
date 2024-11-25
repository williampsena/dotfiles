#!/usr/bin/env bash
dir="$(pwd)"
base_dir=$(realpath "$(pwd)/..")

source $base_dir/_settings.sh

change_wallpaper=$1

options="󰑓 Change Wallpaper\n Cancel"

chosen=$(echo -e "$options" | rofi  -dmenu -p "Menu" -theme ${dir}/theme.rasi)

case "$chosen" in
    "󰑓 Change Wallpaper")
        eval $change_wallpaper
        ;;
    " Cancel")
        exit 1
        ;;
esac
