#!/usr/bin/python
# Source: http://talk.maemo.org/showpost.php?p=1298790&postcount=900
#----------------------------------------------------------------
# Name:        active_rule_names.py
# Purpose:     Print active profilematic rules except default rule
#
# Author:      Slarti
#
# Created:     26.11.2012
#----------------------------------------------------------------

import dbus
bus = dbus.SessionBus()
rule_obj = bus.get_object('org.ajalkane.profilematic', '/org/ajalkane/profilematic')
rule_intf = dbus.Interface(rule_obj, 'org.ajalkane.profilematic')
active_rule_ids = rule_intf.getMatchingRuleIds()
rule_names = rule_intf.getRuleNames()
lookup = []

for rule_name in rule_names:
    rule_id = rule_intf.getRuleIdForName(rule_name)
    lookup.append([rule_id, rule_name])

lookup_dict = dict(lookup)

for active_rule_id in active_rule_ids:
    active_rule_name = lookup_dict[active_rule_id]
    if active_rule_name == 'Default rule':
        continue
    print active_rule_name.encode('utf-8')

