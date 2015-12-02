#!/usr/bin/env python
# encoding: utf-8

class Implementor:
    def Operation(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation(self):
        print "具体实现A的方法执行"

class ConcreteImplementorB(Implementor):
    def operation(self):
        print "具体实现B的方法执行"

class Abstraction:
    def __init__(self):
        self.implementor = None

    def set_implementor(self,  implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.operation()

class RefinedAbstraction(Abstraction):
    def operation(self):
        self.implementor.operation()
        print "this is RefinedAbstraction operation"


ab = RefinedAbstraction()
ia = ConcreteImplementorA()
ab.set_implementor(ia)
ab.operation()
ib = ConcreteImplementorB()
ab.set_implementor(ib)
ab.operation()
