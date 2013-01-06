#!/bin/sh
# Reset the data counter on a selected reset day
# Author: EmaNymton
# Source: http://talk.maemo.org/showpost.php?p=1311100&postcount=448

reset_day="05" # change to your needs
day_of_month=$(date +"%d")
datetime=$(date +"%d.%m.%Y.%s")

if [ $reset_day = $day_of_month ]
then
gconftool -s --type string /cellui/settings/datacounter/transfer/gprs_home_tx_bytes "0"
gconftool -s --type string /cellui/settings/datacounter/transfer/gprs_home_rx_bytes "0"
gconftool -s --type string /cellui/settings/datacounter/general/gprs_home_last_reset $datetime
fi
