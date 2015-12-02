#!/usr/bin/env python
# encoding: utf-8

import copy

class Prototype:
    def __init__(self, id):
        print "this is the init"
        self.id = id

    def pprint(self):
        print "id is ", self.id

    def clone(self):
        pass

class ConcretePrototypeA(Prototype):
    def clone(self):
        return copy.deepcopy(self)

a = ConcretePrototypeA([1,2,3])
b = a.clone()
b.id.append(4)
a.pprint()
b.pprint()

