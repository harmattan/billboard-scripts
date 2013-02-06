#!/usr/bin/python
# Days Remaining in the Current Year
# Author: Thomas Perl

import datetime

today = datetime.datetime.now()
day_of_year = int(today.strftime('%j'))

# Leap year check will work until 2100 (mod 100 and mod 400 rules ignored)
# See http://en.wikipedia.org/wiki/Leap_year#Algorithm
leap_year = (today.year % 4 == 0)

print (366 if leap_year else 365) - day_of_year

