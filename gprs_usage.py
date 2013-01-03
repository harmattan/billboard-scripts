#!/usr/bin/python
# -*- coding: utf-8 -*-
# Show used traffic (requires python-gconf)
# Author: EmaNymton
# Source: http://talk.maemo.org/showpost.php?p=1309409&postcount=401

import gconf
import sys

client = gconf.client_get_default()
tx_bytes = client.get_string('/cellui/settings/datacounter/transfer/gprs_home_tx_bytes')
rx_bytes = client.get_string('/cellui/settings/datacounter/transfer/gprs_home_rx_bytes')
output_string = "up: {tx:03.2f} MB, down: {rx:03.2f} MB".format(tx=float(tx_bytes)/1000000,
                                                                  rx=float(rx_bytes)/1000000)
sys.stdout.write(output_string)
