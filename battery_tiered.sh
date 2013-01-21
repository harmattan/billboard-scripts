#!/bin/sh

# Display Battery Percentage with a Colored Bar in tiered range #
# Author: thedead1440

status=$(qdbus --system org.freedesktop.Hal /org/freedesktop/Hal/devices/bme org.freedesktop.Hal.Device.GetProperty battery.charge_level.percentage)
if [[ $status -ge 50 ]]
then
echo -n "{{green}} Battery $status % " "{{=0.$status}}"
else if [[ $status -ge 25 && $staus -le 49 ]]
then
echo -n "{{yellow}} Battery $status % " "{{=0.$status}}"
else if [[ $status -le 24 ]]
then 
echo -n "{{red}} Battery $status % " "{{=0.$status}}"
fi
fi
fi
