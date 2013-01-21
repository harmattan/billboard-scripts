#!/bin/sh

# Get Data usage + Warn if <20% left with a colored bar #
# Author: thedead1440

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
totalMB=$((($tx+$rx)/1000000))
avail=$(gconftool -g /cellui/settings/datacounter/general/gprs_home_notification_period_UI)
availMB=$(($avail/1000000))
usage=$(($totalMB*100/$availMB))
if [ $usage -ge 80 ]
then
echo {{red}}"Data < 20%" "{{=0.$usage}}"
else 
echo {{cyan}}"Data $totalMB MB" "{{=0.$usage}}" 
fi
