#!/bin/sh
# Show Free and Total Mass Storage Space
# Author: deseven
# Source: http://talk.maemo.org/showpost.php?p=1299193&postcount=289

df -hP | awk '/MyDocs/ { print "disk: " $4 "/" $2 }'

