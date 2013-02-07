#!/usr/bin/python
# Days of Year
# Author: Thomas Perl

import datetime

today = datetime.datetime.now()
day_of_year = int(today.strftime('%j'))

print day_of_year

