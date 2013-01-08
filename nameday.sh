#!/bin/sh
# Output a different text each day
# Author: Thomas Perl
# Source: http://talk.maemo.org/showpost.php?p=1312300&postcount=456

# You need to have a file "nameday.txt" in /home/user (or change the path
# below) that has "DD.MM. TEXT" on each line. "TEXT" will be printed if the
# current date evaluates to DD.MM. Example line (without the leading "# "):
# 08.01. Erland

FILE=/home/user/nameday.txt

awk "/^$(date +%d.%m.)/ { print "'$2'" }" $FILE

