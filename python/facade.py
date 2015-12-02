#!/usr/bin/env python
# encoding: utf-8

class SubSystemA:
    def pprint(self):
        print "this is SubSystemA"

class SubSystemB:
    def pprint(self):
        print "this is SubSystemB"

class SubSystemC:
    def pprint(self):
        print "this is SubSystemC"

class SubSystemD:
    def pprint(self):
        print "this is SubSystemD"

class Facade:
    def __init__(self):
        self.a = SubSystemA()
        self.b = SubSystemB()
        self.c = SubSystemC()
        self.d = SubSystemD()

    def methodA(self):
        self.a.pprint()
        self.b.pprint()
        self.d.pprint()

    def methodB(self):
        self.d.pprint()
        self.c.pprint()
        self.d.pprint()

f = Facade()
f.methodA()
f.methodB()
