#!/bin/sh
# Show Free and Total Memory (RAM)
# Author: deseven
# Source: http://talk.maemo.org/showpost.php?p=1299193&postcount=289

free=$(awk '/MemFree/ {printf( "%.0f\n", $2 / 1024 )}' /proc/meminfo)
cached=$(awk '/^Cached/ {printf( "%.0f\n", $2 / 1024 )}' /proc/meminfo)
buffers=$(awk '/^Buffers/ {printf( "%.0f\n", $2 / 1024 )}' /proc/meminfo)
total=$(awk '/MemTotal/ {printf( "%.0f\n", $2 / 1024 )}' /proc/meminfo)

echo "FreeMem: $((free + cached + buffers))/${total}M"

