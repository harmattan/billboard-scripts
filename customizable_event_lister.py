#!/usr/bin/python
# NOTE THIS WON'T SHOW EVENTS OR TODOS WITHOUT ALARMS
# Print various attributes of events(s) by modifying various things.
# Author: Slarti

import dbus
from datetime import datetime, timedelta, date

bus = dbus.SystemBus()

time_obj = bus.get_object('com.nokia.time', '/com/nokia/time')
time_intf = dbus.Interface(time_obj, 'com.nokia.time')
cookies = (time_intf.get_cookies_by_attributes({'type':'event'}))+(time_intf.get_cookies_by_attributes({'type':'todo'}))
events_list = []
for cookie in cookies:
  attributes = time_intf.query_attributes(cookie)
	timestamp = datetime.strptime((attributes['time']).split('+')[0],
			'%Y-%m-%dT%H:%M:%S')
	events_list.append((timestamp,attributes))

events_list.sort()

# Change these to your own language in the order 
# they are in if you want to print the weekday:

abb_weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# Choose how many days in to the future you want to
# display events.

days_ahead = 7

# Choose the limit for the number of events (lines) to print:

limit = 5

# If you want to print "No events for x days", if there are none,
# leave this as is (the string can be changed).
# If you don't want it, comment this out or delete it:

if (datetime.now() + timedelta(days_ahead)) < events_list[0][0]:
	print ('No events for %s days' % (days_ahead)).encode('utf-8')

# Don't touch this:

if len(events_list) < limit:
	limit = len(events_list)

# This generates what to print on every line:

for i in range(limit):

# Don't touch these:

	event_timestamp = events_list[i][0]
	event_alarm_timestamp = datetime.strptime((events_list[i][1]
				['alarmtime']).split('+')[0], '%Y-%m-%dT%H:%M:%S')

# You can choose from these: (Date and time formats can be
# changed. Google how with "datetime.strftime format")

	if events_list[i][1]['type'] == 'todo':
		event_type = 'todo'
	else:
		event_type = 'event'
	event_date = datetime.strftime(event_timestamp,"%d.%m.")
	event_time = datetime.strftime(event_timestamp,"%H:%M")
	weekday = abb_weekdays[date.weekday(event_timestamp)]
	title = events_list[i][1]['TITLE']
	alarmtime = datetime.strftime(event_alarm_timestamp,"%H:%M")
        time_to_event = ':'.join(str(event_timestamp - datetime.now())
			.split(':')[:2])
	if 'location' in events_list[i][1]:
		location = events_list[i][1]['location']
	else:
		location = ''

# This is the special character. Look for the Python source code
# string at e.g. http://www.fileformat.info/info/unicode/block/index.htm

	sc = u"\u2691"

# Don't touch this. It evaluates if the event is within the set time limit.

	if (event_timestamp - datetime.now()) <= timedelta(days=days_ahead):

# Here you can decide what to print in which order.
# If you want to add a color enclose it in quotes '{{green}}'	
	
		print (event_type+' '+event_date+' '+event_time+' '+weekday+' '+title+' '
			+location+' '+alarmtime+' '+time_to_event+' '+sc).encode('utf-8')
