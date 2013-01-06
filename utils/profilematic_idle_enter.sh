#!/bin/sh
# Profilematic idle enter script
# Author: coderus
# Source: http://talk.maemo.org/showpost.php?p=1310747&postcount=428

# Script for force updating Billboard data when locking screen. Should be used
# with profilematic idle rule as activate script.

text=$(gconftool -g /apps/billboard/text)
gconftool -s -t string /apps/billboard/text "{{white}}Updating..."
gconftool -s -t string /apps/billboard/text "${text}"

