#!/usr/bin/python
#
# Show estimated remaining battery time
#
# Depends on: python-qmsystem
# Author: coderus, with slight modifications
# Source: http://talk.maemo.org/showpost.php?p=1322882&postcount=604
#

import QmSystem

battery = QmSystem.QmBattery()

#time = battery.getRemainingIdleTime(QmSystem.QmBattery.NormalMode)
time = battery.getRemainingTalkTime(QmSystem.QmBattery.NormalMode)

hours, remaining = divmod(time, 60*60)
minutes, seconds = divmod(remaining, 60)

result = []

if hours == 1:
    result.append('%d hour' % hours)
elif hours > 0:
    result.append('%d hours' % hours)

if minutes == 1:
    result.append('%d minute' % minutes)
elif minutes > 0 or not result:
    result.append('%d minutes' % minutes)

print ' '.join(result)

