#!/bin/bash

export QTILE_HOME=$HOME/.config/qtile

function get_yaml_value() {
    key="$1"
    yaml_file="$QTILE_HOME/config.yml"
    value=$(yq -r $key $yaml_file)
    echo $value
}
