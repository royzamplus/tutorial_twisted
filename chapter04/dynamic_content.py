#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

import time


class ClockPage(Resource):
    isLeaf = True   # isLeaf describes whether or not a resource will have children

    def render_GET(self, request):
        return "The local time is %s" % (time.ctime(),)

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()