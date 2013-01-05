#!/bin/sh
# Print bluetooth status icon off/disconnected/connected
# Show the correct icon for connected or disconnected states.
# No icon is shown when BT is off.
#
# Author: coderus
# Source: http://talk.maemo.org/showpost.php?p=1311091&postcount=447

powered=$(qdbus --system org.bluez $(qdbus --literal --system org.bluez / org.bluez.Manager.ListAdapters | sed -re "s/.*(\/org\/bluez\/[0-9]{4}\/hci0).*/\1/") org.bluez.Adapter.GetProperties $
connected=$(qdbus --system com.nokia.policy.pcfd /com/nokia/policy/bluetooth_override org.maemo.contextkit.Property.Get | sed -n 1p)
if [ "$powered" == "true" ]; then
        if [ "$connected" == "default" ]; then
                echo -n "<</usr/share/themes/blanco/meegotouch/icons/icon-s-status-bluetooth-active.png>>"
        else
                echo -n "<</usr/share/themes/blanco/meegotouch/icons/icon-s-status-bluetooth.png>>"
        fi
fi
