#!/bin/sh
# Get total GPRS transmission in MB
# Author: thedead1440
# Source: http://talk.maemo.org/showpost.php?p=1309420&postcount=402

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
total=$((($tx+$rx)/1000000))
echo "Data used = $total MB"
