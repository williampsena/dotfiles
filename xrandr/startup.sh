#!/usr/bin/env bash
MODE=$1

function run {
    if ! pgrep $1 ; then
        $@&
    fi
}

if xrandr | grep -q 'VGA-1 connected' ; then
    xrandr --output VGA-1 --mode $MODE --left-of eDP1
fi

if xrandr | grep -q 'HDMI1 connected' ; then
    xrandr --output HDMI1 --mode $MODE --left-of eDP1
fi
