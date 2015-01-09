#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File('/home/roy/Projects/twisted_tutorial')
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()