#!/usr/bin/env python
# encoding: utf-8

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print "this is the real request"

class ProxySubject(Subject):
    def __init__(self):
        self.realone = None

    def request(self):
        if not self.realone:
            self.realone = RealSubject()

        print "this is the proxy request"
        self.realone.request()
        print "proxy end"

sub = ProxySubject()

sub.request()
