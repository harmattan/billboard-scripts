#!/bin/sh
# Load Average
# Author: deseven
# Source: http://talk.maemo.org/showpost.php?p=1299193&postcount=289

cat /proc/loadavg | cut -f1,2,3 -d" "

