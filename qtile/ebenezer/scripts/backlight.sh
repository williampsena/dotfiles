#!/bin/bash

backlight_level() {
    brightnessctl | grep -oP '\d+%'
}

backlight_up() {
    brightnessctl set 10%+
}

backlight_down() {
    brightnessctl set 10%-
}

option=$1

case $option in
level)
    backlight_level
    ;;
up)
    backlight_up
    ;;
down)
    backlight_down
    ;;
*)
    echo "Usage: $0 {level|up|down}"
    exit 1
    ;;
esac
