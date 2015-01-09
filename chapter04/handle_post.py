#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

import cgi

class FormPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return """
<html>
 <body>
  <form method="POST">
   <input name="form-field" type="text" />
   <input type="submit" />
   </form>
   </body>
   </html>
"""

    def render_POST(self, request):
        return """
<html>
 <body>You submitted: %s</body>
 </html>
""" % (cgi.escape(request.args[form-field][0]),)


factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()