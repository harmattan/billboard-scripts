#!/usr/bin/python
#
# Show connected clients using SSH ("SDK mode")
#
# Author: thp
# Request: http://talk.maemo.org/showpost.php?p=1354336&postcount=905
#

import subprocess

"""
Example output of 'who' on Harmattan:

user            pts/0           00:00   Jun 24 09:25:38  192.168.2.14
"""

who = [line.split() for line in subprocess.Popen(['who'],
    stdout=subprocess.PIPE).communicate()[0].splitlines()]
print (('%d user%s connected: %s' % (len(who), 's' * (len(who) != 1),
        ', '.join('%s (%s)' % (x[0], x[-1]) for x in who)))
        if who else 'no users connected')

