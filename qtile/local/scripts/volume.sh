#!/bin/bash

volume_level() {
    pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\+'
}

volume_up() {
    pactl set-sink-volume @DEFAULT_SINK@ +5%
}

volume_down() {
    pactl set-sink-volume @DEFAULT_SINK@ -5%
}

mute_toggle() {
    pactl set-sink-mute @DEFAULT_SINK@ toggle
}

mute_on() {
    pactl set-sink-mute @DEFAULT_SINK@ 1
}

mute_off() {
    pactl set-sink-mute @DEFAULT_SINK@ 0
}

mute_status() {
    pactl list sinks | grep 'Mute:' | head -n 1 | awk '{print $2}'
}

option=$1

case $option in
level)
    volume_level
    ;;
up)
    volume_up
    ;;
down)
    volume_down
    ;;
mute)
    mute_toggle
    ;;
mute_on)
    mute_on
    ;;
mute_off)
    mute_off
    ;;
mute_status)
    mute_status
    ;;
*)
    echo "Usage: $0 {level|up|down|mute|mute_on|mute_off|mute_status}"
    exit 1
    ;;
esac
