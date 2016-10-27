#!/usr/bin/python

from __future__ import print_function

import sys
import time
import random

import clockapi

# Tweet immediately in 420 mode. Otherwise, be lazy and wait to tweet.
if len(sys.argv) > 1:
    ftmode = True
else:
    ftmode = False
    # Wait randomly between 2 and 25 minutes
    time.sleep(60*random.randint(3,15))

if ftmode:
    clockapi.post(msg='BONG!!!!!!')
else:
    clockapi.post()

