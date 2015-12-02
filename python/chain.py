#!/usr/bin/env python
# encoding: utf-8

class Handler:
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request >= 0 and request < 10:
            print "this is %s handle the request"% self.__class__,request
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request >= 10 and request < 20:
            print "this is %s handle the request"% self.__class__,request
        elif self.successor:
            self.successor.handle_request(request)
class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request >= 20 and request < 30:
            print "this is %s handle the request"% self.__class__,request
        elif self.successor:
            self.successor.handle_request(request)
class ConcreteHandlerD(Handler):
    def handle_request(self, request):
        print "this is %s handle the request"% self.__class__,request

a = ConcreteHandlerA()
b = ConcreteHandlerB()
c = ConcreteHandlerC()
d = ConcreteHandlerD()
a.set_successor(b)
b.set_successor(c)
c.set_successor(d)

requests = [2,3,12,34,25,34,23,9,6,4]
for r in requests:
    a.handle_request(r)
