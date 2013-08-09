#!/bin/sh
# Get GPRS roaming transmission separated in up&down in MB
# Author: thedead1440
# Source: http://talk.maemo.org/showpost.php?p=1309420&postcount=402

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_roaming_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_roaming_rx_bytes)
txMB=$(($tx/1000000))
rxMB=$(($rx/1000000))
echo "up: $txMB MB, down: $rxMB MB"
