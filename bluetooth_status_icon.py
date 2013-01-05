#!/usr/bin/python
# Print bluetooth status icon off/disconnected/connected
# Show the correct icon for connected or disconnected states.
# No icon is shown when BT is off.
#
# Author: Slarti
# Source: http://talk.maemo.org/showpost.php?p=1311023&postcount=444

import dbus

bus = dbus.SystemBus()

bluez = bus.get_object('org.bluez', '/')
adapter_path = bluez.ListAdapters(dbus_interface='org.bluez.Manager')[0]
adapter = bus.get_object('org.bluez', adapter_path)
powered = adapter.GetProperties(dbus_interface='org.bluez.Adapter')['Powered']
btstatus = bus.get_object('com.nokia.policy.pcfd', '/com/nokia/policy/bluetooth_override')
connected = btstatus.Get(dbus_interface='org.maemo.contextkit.Property')[0]

if powered:
    if 'default' in connected:
        print '<</usr/share/themes/blanco/meegotouch/icons/icon-s-status-bluetooth-active.png>>'
    else:
        print '<</usr/share/themes/blanco/meegotouch/icons/icon-s-status-bluetooth.png>>'

