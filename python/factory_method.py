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

class FactoryBase:
    def  __init__(self):
        print "this is the FactoryBase"

    @staticmethod
    def create():
        pass

class FactoryA(FactoryBase):
    @staticmethod
    def create():
        instance = ConstantA()
        return instance

class FactoryB(FactoryBase):
    @staticmethod
    def create():
        instance = ConstantB()
        return instance

o1 = FactoryA.create()
o1.operation()
o2 = FactoryB.create()
o2.operation()
