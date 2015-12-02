#!/usr/bin/env python
# encoding: utf-8

class Base():
    def __init__(self):
        print "this is the base"

    def operation(self):
        pass

class ConstantA(Base):
    def __init__(self):
        Base.__init__(self)
        print "this is the ConstantA"

    def operation(self):
        print "this is A's operation"

class ConstantB(Base):
    def __init__(self):
        Base.__init__(self)
        print "this is the ConstantB"

    def operation(self):
        print "this is B's operation"

class SimpleFactory:
    def  __init__(self):
        print "this is the SimpleFactory"

    @staticmethod
    def foo(type = 'A'):
        if type == 'A':
            instance = ConstantA()
        elif type == 'B':
            instance = ConstantB()
        else:
            instance = None


        return instance

o1 = SimpleFactory.foo('A')
o1.operation()
o2 = SimpleFactory.foo('B')
o2.operation()
o3 = SimpleFactory.foo('C')
o3.operation()

