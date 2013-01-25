#!/bin/sh

# Display Battery Percentage with a Colored Bar in tiered range #
# Author: thedead1440
# Bar range corrected by Thomas Perl aka thp

status=$(qdbus --system org.freedesktop.Hal /org/freedesktop/Hal/devices/bme org.freedesktop.Hal.Device.GetProperty battery.charge_level.percentage)
if [[ $status -ge 50 ]]
then
echo -n "{{green}} Battery $status % " "{{=$(($status/100)).$((($status%100)/10))$(($status%10))}}"
else if [[ $status -ge 25 && $staus -le 49 ]]
then
echo -n "{{yellow}} Battery $status % " "{{=$(($status/100)).$((($status%100)/10))$(($status%10))}}"
else if [[ $status -le 24 ]]
then 
echo -n "{{red}} Battery $status % " "{{=$(($status/100)).$((($status%100)/10))$(($status%10))}}"
fi
fi
fi
