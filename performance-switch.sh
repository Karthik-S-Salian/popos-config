#!/bin/bash

BATTERY="BAT0"
AC="ADP1"

BAT_PATH="/sys/class/power_supply/$BATTERY"
AC_PATH="/sys/class/power_supply/$AC"

[ -d "$BAT_PATH" ] || exit 0
[ -d "$AC_PATH" ] || exit 0

capacity=$(cat "$BAT_PATH/capacity")
online=$(cat "$AC_PATH/online")

if [ "$online" -eq 1 ] && [ "$capacity" -eq 100 ]; then
    notify-send "Power Profile" "Performance mode enabled"
    system76-power profile performance

elif [ "$online" -eq 1 ]; then
    notify-send "Power Profile" "Balanced mode enabled"
    system76-power profile balanced

else
    notify-send "Power Profile" "Battery mode enabled"
    system76-power profile battery
fi
