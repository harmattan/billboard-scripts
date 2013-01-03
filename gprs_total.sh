#!/bin/sh

# Get total GPRS transmission in MB

tx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_tx_bytes)
rx=$(gconftool -g /cellui/settings/datacounter/transfer/gprs_home_rx_bytes)
total=$((($tx+$rx)/1000000))
echo "Data used = $total MB"
