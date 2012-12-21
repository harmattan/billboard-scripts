#!/usr/bin/python
# List upcoming alarms on MeeGo 1.2 Harmattan
# Thanks to slarti on TMO for figuring out the D-Bus methods
# Thomas Perl <thp.io/about>; 2012-06-13
# from http://talk.maemo.org/showpost.php?p=1221428&postcount=91

import dbus

bus = dbus.SystemBus()

time_obj = bus.get_object('com.nokia.time', '/com/nokia/time')
time_intf = dbus.Interface(time_obj, 'com.nokia.time')

cookies = time_intf.get_cookies_by_attributes({'enabled': '1'})

def get_queued_alarms():
    for cookie in cookies:
        attributes = time_intf.query_attributes(cookie)
        if attributes['STATE'] == 'QUEUED':
            yield ' '.join((attributes['alarmtime'],
                            attributes['TITLE']))

print '\n'.join(sorted(get_queued_alarms())) or 'No alarms'

