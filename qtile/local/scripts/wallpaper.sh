#!/bin/bash

random_wallpaper() {
   local wallpaper_dir=$1
   local timeout=${2:-1800}

   while true; do
      set_wallpaper $wallpaper_dir
      sleep $timeout
   done
}

set_wallpaper() {
   local wallpaper_dir=$1
   feh --bg-scale --randomize $wallpaper_dir*
}

option=$1

case $option in
set)
   set_wallpaper $2
   ;;
slideshow)
   random_wallpaper $2 $3
   exit 1
   ;;
*)
   echo "Usage: $0 {set|slideshow}"
   exit 1
   ;;
esac
