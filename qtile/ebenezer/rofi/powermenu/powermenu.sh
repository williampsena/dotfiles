#!/usr/bin/env bash
source ./_settings.sh

dir="$(pwd)"

lock_command=$(get_ini_value "lock_screen" "command")
uptime=$(uptime -p | sed -e 's/up //g')

rofi_command="rofi -theme $dir/powermenu.rasi"

# Options
hibernate='󱡓'
shutdown='󰐥'
reboot=''
lock=''
suspend=''
logout='󰍃'
yes='󰗡'
no='󰜺'

confirm_cmd() {
	rofi -theme-str 'window {location: center; anchor: center; fullscreen: false; width: 350px;}' \
		-theme-str 'mainbox {orientation: vertical; children: [ "message", "listview" ];}' \
		-theme-str 'listview {columns: 2; lines: 1;}' \
		-theme-str 'element-text {horizontal-align: 0.5;}' \
		-theme-str 'textbox {horizontal-align: 0.5;}' \
		-dmenu \
		-p 'Confirmation' \
		-mesg 'Are you Sure?' \
		-theme ${dir}/confirm.rasi
}

confirm_exit() {
	echo -e "$yes\n$no" | confirm_cmd
}

shutdown() {
	selected="$(confirm_exit)"
	if [[ "$selected" == "$yes" ]]; then
		systemctl poweroff
	fi
}

reboot() {
	selected="$(confirm_exit)"
	if [[ "$selected" == "$yes" ]]; then
		systemctl reboot
	fi
}

hibernate() {
	systemctl hibernate
}

suspend() {
	amixer set Master mute
	systemctl suspend
}

lock_screen() {
	close_rofi
	eval $lock_command
}

logout() {
	qtile cmd-obj -o cmd -f shutdown &
}

close_rofi() {
	pkill ^rofi
	sleep 0.5
}

chosen="$(echo -e "$shutdown\n$reboot\n$lock\n$suspend\n$logout" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 2)"
case $chosen in
$shutdown)
	shutdown
	;;
$reboot)
	reboot
	;;
$lock)
	lock_screen
	;;
$suspend)
	suspend
	;;
$logout)
	logout
	;;
esac
