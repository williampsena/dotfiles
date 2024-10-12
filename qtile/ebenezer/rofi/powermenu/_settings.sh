#!/bin/bash

export QTILE_HOME=$HOME/.config/qtile

function get_ini_value() {
    section=$1
    key=$2
    ini_file="$QTILE_HOME/config.ini"
    value=$(sed -nr "/^\[$section\]/ { :l /^$key[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" $ini_file)
    echo $value
}
