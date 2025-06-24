#!/bin/bash

WALLPAPER_DIR="$HOME/Pictures/Wallpapers/Active"
MONITOR_NAME="eDP-1"

CONFIG_FILE="$HOME/.config/hypr/hyprpaper.conf"

echo "" > "$CONFIG_FILE"

for img in "$WALLPAPER_DIR"/*.{jpg,jpeg,png}; do
    [ -e "$img" ] || continue
    echo "preload = $img" >> "$CONFIG_FILE"
done

FIRST_IMG=$(ls "$WALLPAPER_DIR"/*.{jpg,jpeg,png} | head -n 1)
echo "wallpaper = $MONITOR_NAME,$FIRST_IMG" >> "$CONFIG_FILE"
echo "slideshow = true" >> "$CONFIG_FILE"
echo "slideshow_interval = 30" >> "$CONFIG_FILE"

echo "Arquivo $CONFIG_FILE gerado com sucesso."

