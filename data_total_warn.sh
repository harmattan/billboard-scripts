#!/bin/sh

# Get Data usage + Warn if <20% left with a colored bar #
# Author: thedead1440
# Bar corrected by Thomas Perl aka thp

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
totalMB=$((($tx+$rx)/1000000))
avail=$(gconftool -g /cellui/settings/datacounter/general/gprs_home_notification_period_UI)
availMB=$(($avail/1000000))
usage=$(($totalMB*100/$availMB))
if [ $usage -ge 80 ]
then
echo {{red}}"Data < 20%" "{{=$(($usage/100)).$((($usage%100)/10))$(($usage%10))}}"
else 
echo {{cyan}}"Data $totalMB MB" "{{=$(($usage/100)).$((($usage%100)/10))$(($usage/10))}}"
fi
