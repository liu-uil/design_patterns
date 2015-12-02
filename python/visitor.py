#!/usr/bin/env python
# encoding: utf-8

class Visitor:
    def visit_ConcreteElementA(self, concreteA):
        pass

    def visit_ConcreteElementB(self, concreteB):
        pass


class ConcreteVisitorA(Visitor):
    def visit_ConcreteElementA(self, concreteA):
        print "%s 被 %s 访问了"%(concreteA.__class__, self.__class__)

    def visit_ConcreteElementB(self, concreteB):
        print "%s 被 %s 访问了"%(concreteB.__class__, self.__class__)

class ConcreteVisitorB(Visitor):
    def visit_ConcreteElementA(self, concreteA):
        print "%s 被 %s 访问了"%(concreteA.__class__, self.__class__)

    def visit_ConcreteElementB(self, concreteB):
        print "%s 被 %s 访问了"%(concreteB.__class__, self.__class__)

class Element:
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_ConcreteElementA(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_ConcreteElementB(self)

class ObjectStructure:
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for item in self.elements:
            item.accept(visitor)


o = ObjectStructure()
o.attach(ConcreteElementA())
o.attach(ConcreteElementB())
o.attach(ConcreteElementA())
v1 = ConcreteVisitorA()
v2 = ConcreteVisitorB()
o.accept(v1)
o.accept(v2)

