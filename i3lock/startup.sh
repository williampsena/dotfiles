timeout=${LOCK_SCREEN_TIMEOUT:-30}

if pgrep -x "xautolock" >/dev/null
then
    pkill xautolock
fi

xautolock -detectsleep -time $timeout -locker "$HOME/.config/i3lock/run.sh"