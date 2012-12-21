#!/usr/bin/python
# List upcoming alarms on MeeGo 1.2 Harmattan
# Thanks to slarti on TMO for figuring out the D-Bus methods
# Thomas Perl <thp.io/about>; 2012-06-13
# Horribly mangled by slarti to find only the next alarm
# (set from clock application); 2012-06-19
# from http://talk.maemo.org/showpost.php?p=1224180&postcount=107

import dbus
from datetime import datetime, timedelta
import time

bus = dbus.SystemBus()

time_obj = bus.get_object('com.nokia.time', '/com/nokia/time')
time_intf = dbus.Interface(time_obj, 'com.nokia.time')

cookies = time_intf.get_cookies_by_attributes({'enabled': '1'})
today = datetime.now()
tomorrow = today + timedelta(days=1)

def list_queued_alarms():
    for cookie in cookies:
        attributes = time_intf.query_attributes(cookie)
        alarmtime = attributes['alarmtime']
        if attributes['STATE'] == 'QUEUED':
            if 'recurrence' in attributes:
                days = tuple(attributes['recurrence'])
            else:
                if datetime.time(datetime.strptime(alarmtime, ("%H:%M"))) > datetime.time(datetime.now()):
                    days = time.strftime("%w")
                else:
                    days = tomorrow.strftime("%w")
            weekdays = dict([(day, time.strptime((day + " " + alarmtime),'%w %H:%M' )) for day in days])
            for day in days:
                yield ' '.join((day,time.strftime('%a %H:%M',weekdays[day]),attributes['TITLE']))


findme_list = [' '.join((time.strftime('%w %a %H:%M'),'findme'))]
L = list(list_queued_alarms()) + findme_list
L.sort()
findme_string = ' '.join((time.strftime('%w %a %H:%M'),'findme'))
findme_int = L.index(findme_string)
if len(L) == 1:
    next_alarm = 'xxNo alarms'
else:
    if findme_int == (len(L) - 1):
        next_alarm = L[0]
    else:
        next_alarm = L[findme_int + 1]

print next_alarm[2:]
