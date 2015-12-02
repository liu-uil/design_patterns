#!/usr/bin/env python
# encoding: utf-8

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        for p in self.parts:
            print "this is part:", p

class Builder:
    def buildPartA(self):
        pass
    def buildPartB(self):
        pass

    def getResult(self):
        pass

class ConcreteBuilderA(Builder):
    def __init__(self):
        self.product = Product()

    def buildPartA(self):
        self.product.add('parta in A')

    def buildPartB(self):
        self.product.add('partb in A')

    def getResult(self):
        return self.product

class ConcreteBuilderB(Builder):
    def __init__(self):
        self.product = Product()

    def buildPartA(self):
        self.product.add('parta in B')

    def buildPartB(self):
        self.product.add('partb in B')

    def getResult(self):
        return self.product

class Director:
    def construct(self, builder):
        builder.buildPartA()
        builder.buildPartB()

d = Director()
aa = ConcreteBuilderA()
bb = ConcreteBuilderB()
d.construct(aa)
d.construct(bb)
productA = aa.getResult()
productB = bb.getResult()
productA.show()
productB.show()

