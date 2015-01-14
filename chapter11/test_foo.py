#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.trial import unittest

class MyFirstTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue