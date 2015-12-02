#!/usr/bin/env python
# encoding: utf-8

class Target:
    def request(self):
        print "this is normal request"


class Adaptee:
    def special_request(self):
        print "this is special request"

class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.special_request()


t = Adapter()
t.request()

