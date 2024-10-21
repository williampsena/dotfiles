#!/usr/bin/env bash
base_dir=$(realpath "$(pwd)/..")
dir="$(pwd)"

title=${1:-Confirmation}
question=${2:-Are you sure?}

# Options
yes='󰩐'
no=''

confirm_cmd() {
	rofi -theme-str 'window {location: center; anchor: center; fullscreen: false; width: 350px;}' \
		-theme-str 'mainbox {orientation: vertical; children: [ "message", "listview" ];}' \
		-theme-str 'listview {columns: 2; lines: 1;}' \
		-theme-str 'element-text {horizontal-align: 0.5;}' \
		-theme-str 'textbox {horizontal-align: 0.5;}' \
		-dmenu \
		-p "$title" \
		-mesg "$question" \
		-theme ${dir}/confirm.rasi
}

choice=$(echo -e "$yes\n$no" | confirm_cmd)

if [[ $choice == "$yes" ]]; then
	echo "yes"
else
	echo "no"
fi
