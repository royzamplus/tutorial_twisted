#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred

def myCallback(result):
    print result

d = Deferred()
d.addCallback(myCallback)
d.callback('Triggering callback.')