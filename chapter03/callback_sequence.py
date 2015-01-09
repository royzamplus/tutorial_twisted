#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.defer import Deferred

def callback1(result):
    print "Callback 1 said:", result
    return result

def callback2(result):
    print "Callback 2 said:", result

def callback3(result):
    raise Exception("Callback 3")

def errback1(failure):
    print "Errback 1 had an error on", failure
    return failure

def errback2(failure):
    raise Exception("Errback 2")

def errback3(failure):
    print "Errback 3 took care of", failure
    return "Everything is fine now."

# exercise 1
#d = Deferred()
#d.addCallback(callback1)
#d.addCallback(callback2)
#d.callback("Test")

# exercise 2
#d = Deferred()
#d.addCallback(callback1)
#d.addCallback(callback2)
#d.addCallback(callback3)
#d.callback("Test")

# exercise 3
#d = Deferred()
#d.addCallback(callback1)
#d.addCallback(callback2)
#d.addCallback(callback3)
#d.addErrback(errback3)
#d.callback("Test")

# exercise 4
#d = Deferred()
#d.addErrback(errback1)
#d.errback("Test")

# exercise 5
#d = Deferred()
#d.addErrback(errback1)
#d.addErrback(errback3)
#d.errback("Test")

# exercise 6
d = Deferred()
d.addErrback(errback2)
d.errback("Test")