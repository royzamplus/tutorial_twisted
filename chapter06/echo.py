#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor

"""
A module containing the Protocol and Factory definitions
"""

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()