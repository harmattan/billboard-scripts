#!/bin/sh
# Days Remaining in the Current Year
# Author: Thomas Perl

# Leap year check will work until 2100 (mod 100 and mod 400 rules ignored)
# See http://en.wikipedia.org/wiki/Leap_year#Algorithm
leap_year=$(($(date +%Y) % 4 == 0))

echo $((365 + $leap_year - $(date +%j)))

