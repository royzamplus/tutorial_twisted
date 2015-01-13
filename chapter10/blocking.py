#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from twisted.internet import reactor, threads
from twisted.internet.task import LoopingCall

def finish():
    reactor.stop()

reactor.callLater(2, finish)
reactor.run()