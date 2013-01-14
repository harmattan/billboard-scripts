#!/usr/bin/python
# Print various attributes of alarm(s) by modifying various things
# Author: slarti

import dbus
from datetime import datetime, timedelta, date

bus = dbus.SystemBus()

time_obj = bus.get_object('com.nokia.time', '/com/nokia/time')
time_intf = dbus.Interface(time_obj, 'com.nokia.time')
alarm_obj = bus.get_object('com.nokia.time', '/org/maemo/contextkit/Alarm/Trigger')
alarms = alarm_obj.Get(dbus_interface='org.maemo.contextkit.Property')[0]
cookies = alarms[0].keys()
alarms_list = []
for cookie in cookies:
        timestamp = alarms[0][cookie]
        attributes = time_intf.query_attributes(cookie)
        alarms_list.append(((timestamp,cookie,attributes)))

alarms_list.sort()

# Change these to your own language in the order
# they are in if you want to print the weekday:

abb_weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# Choose the limit for the number of alarms (lines) to print:

limit = 5

# If you want to print "No alarms", if there are none,
# leave this as is (the string can be changed).
# If you don't want it, comment this out or delete it:

if len(alarms_list) == 0:
        print 'No alarms'

# Don't touch this:

if len(alarms_list) < limit:
        limit = len(alarms_list)

# This generates what to print on every line:

for i in range(limit):

# Don't touch this:

        alarm_timestamp = datetime.fromtimestamp((alarms_list[i][0])/1000000000)

# You can choose from these:

        weekday = abb_weekdays[date.weekday(alarm_timestamp)]
        title = alarms_list[i][2]['TITLE']
        alarmtime = datetime.strftime(alarm_timestamp,"%H:%M")
        time_to_alarm = ':'.join(str(alarm_timestamp - datetime.now()).split(':')[:2])
        snooze = alarms_list[i][2]['snooze']+'min'

# This is the special character. Look for the Python source code
# string at e.g. http://www.fileformat.info/info/unicode/block/index.htm

        sc = u"\u2691"

# Here you can decide what to print in which order:

        print (weekday+' '+title+' '+alarmtime+' '+time_to_alarm+' '+snooze+' '+sc).encode('utf-8')
