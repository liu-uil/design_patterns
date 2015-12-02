#!/usr/bin/env python
# encoding: utf-8

class Base:
    @staticmethod
    def operation():
        pass

class Concrete(Base):
    @staticmethod
    def operation():
        print "this is the Concrete operation"

class Decorator(Base):
    def setComponent(self, component):
        self.component = component

    def operation(self):
        if self.component:
            print "this is operation in Decorator", self.name
            self.component.operation()

class DecoratorA(Decorator):
    def __init__(self):
        self.name = 'DecoratorA'

    def operation(self):
        Decorator.operation(self)
        print "A's operation"

class DecoratorB(Decorator):
    def __init__(self):
        self.name = 'DecoratorB'

    def operation(self):
        Decorator.operation(self)
        print "B's operation"

c = Concrete()
a = DecoratorA()
b = DecoratorB()

a.setComponent(c)
b.setComponent(a)

b.operation()

