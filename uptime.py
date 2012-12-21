#!/usr/bin/python
# Show Device Uptime
# Thomas Perl <thp.io/about>

import datetime

seconds = int(float(open('/proc/uptime').read().split()[0]))
print str(datetime.timedelta(0, seconds))[:-3]

