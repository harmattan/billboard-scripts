#!/bin/sh
# Show current time in different parts of the world
# by thp
# see also http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# from http://talk.maemo.org/showthread.php?p=1297454#post1297454

echo -n "Time in Vienna: "
TZ=Europe/Vienna date +"%F %H:%M"
echo -n "Time in Helsinki: "
TZ=Europe/Helsinki date +"%F %H:%M"
echo -n "Time in London: "
TZ=Europe/London date +"%F %H:%M"

