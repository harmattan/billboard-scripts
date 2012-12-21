#!/bin/sh
# Show icon if alarm is present
# Usage: {script:sh /path/to/script.sh}
# Author: coderus
# from http://talk.maemo.org/showpost.php?p=1304821&postcount=344

reply=$(qdbus --system com.nokia.time /org/maemo/contextkit/Alarm/Present org.maemo.contextkit.Property.Get | sed -n 1p)
if [ "$reply" == "true" ]; then
    echo -n "<</usr/share/themes/blanco/meegotouch/icons/icon-s-alarm-inverse.png>>"
fi

