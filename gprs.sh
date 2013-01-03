#!/bin/sh

# Get GPRS transmission separated in up&down in MB

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
txMB=$(($tx/1000000))
rxMB=$(($rx/1000000))
echo "up: $txMB MB, down: $rxMB MB"
