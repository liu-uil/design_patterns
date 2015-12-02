#!/usr/bin/env python
# encoding: utf-8

class Flyweight:
    def operation(self, extrinsicstate):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self,extrinsicstate):
        print "具体的Flyweight", extrinsicstate

class UnsharedConcreteFlyweight(Flyweight):
    def operation(self,extrinsicstate):
        print "不共享的具体的Flyweight", extrinsicstate

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}
        self.flyweights['x'] = ConcreteFlyweight()
        self.flyweights['y'] = ConcreteFlyweight()
        self.flyweights['z'] = ConcreteFlyweight()

    def get_flyweight(self, key):
        return self.flyweights[key]


e = 22
f = FlyweightFactory()
fx = f.get_flyweight('x')
fx.operation(e)
e -= 1
fy = f.get_flyweight('y')
fy.operation(e)
e -= 1
fz = f.get_flyweight('z')
fz.operation(e)
e -= 1

uf = UnsharedConcreteFlyweight()
uf.operation(e)


