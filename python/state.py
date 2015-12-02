#!/usr/bin/env python
# encoding: utf-8

class State:
    def handle(self):
        pass

class StateA(State):

    def handle(self, context):
        print "this is StateA handle"
        context.state = StateB()

class StateB(State):

    def handle(self, context):
        print "this is StateB handle"
        context.state = StateA()

class Context:
    def __init__(self):
        self.__dict__['state'] = StateA()

    def __setattr__(self, name, val):
        self.__dict__[name] = val
        print "the new state is ", self.state

    def request(self):
        self.state.handle(self)


c = Context()
c.request()
c.request()
c.request()
c.request()
