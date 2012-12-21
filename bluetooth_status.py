#!/usr/bin/python
# Print bluetooth status (on/off)
# Thomas Perl <thp.io/about: 2012-06-07
# from http://talk.maemo.org/showpost.php?p=1218903&postcount=63

import dbus

bus = dbus.SystemBus()

bluez = bus.get_object('org.bluez', '/')
adapter_path = bluez.ListAdapters(dbus_interface='org.bluez.Manager')[0]
adapter = bus.get_object('org.bluez', adapter_path)
powered = adapter.GetProperties(dbus_interface='org.bluez.Adapter')['Powered']

if powered:
    print 'Bluetooth on'
else:
    print 'Bluetooth off'

