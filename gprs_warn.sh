#!/bin/sh
# Warn in red if Data left is less than 20%
# bc is a pre-requisite to be installed from harmattan sdk repo
#
# Author: thedead1440
# Source: http://talk.maemo.org/showpost.php?p=1309420&postcount=402

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
total=$(($tx+$rx))
usage=$(gconftool -g /cellui/settings/datacounter/general/gprs_home_notification_period_UI)
amount=`dc $total $usage / p`

if [ $(echo "$amount > 0.800" |bc) -eq 1 ]
then
echo {{red}}"Data left < 20%"
fi
exit 1
