#!/bin/bash
IMAGE=/tmp/i3lock.png
BLURTYPE="0x5"
BLANK='#00000000'
CLEAR='#ffffff22'
DEFAULT='#9db4c0'
KEY='#8a8ea800'
TEXT='#4BC1CC'
WRONG='#D50000'
VERIFYING='#41445800'

if pgrep -x "i3lock" >/dev/null
then
    echo "i3lock is already running."
    exit 0
fi

scrot $IMAGE
convert $IMAGE -blur $BLURTYPE $IMAGE 
i3lock -i $IMAGE  \
    --insidever-color=$CLEAR \
    --ringver-color=$VERIFYING \
    \
    --insidewrong-color=$WRONG \
    --ringwrong-color=$DEFAULT \
    \
    --inside-color=$CLEAR \
    --ring-color=$DEFAULT \
    --line-color=$BLANK \
    --separator-color=$DEFAULT \
    \
    --verif-color=$TEXT \
    --wrong-color=$TEXT \
    --time-color=$TEXT \
    --date-color=$TEXT \
    --layout-color=$TEXT \
    --keyhl-color=$KEY \
    --bshl-color=$WRONG \
    \
    --indicator \
    --clock \
    --time-str="%H:%M"

rm $IMAGE