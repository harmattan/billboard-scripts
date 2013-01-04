#!/bin/sh
# Uptime Script
# Author: deseven
# Source: http://talk.maemo.org/showpost.php?p=1299193&postcount=289

uptime=$(cat /proc/uptime)
uptime=${uptime%%.*}
m=$(( uptime/60%60 ))
h=$(( uptime/60/60%24 ))
d=$(( uptime/60/60/24 ))
echo "up: "$d"d "$h"h "$m"m"

