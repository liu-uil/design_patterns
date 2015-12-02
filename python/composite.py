#!/usr/bin/env python
# encoding: utf-8

class Component:
    def __init__(self, name):
        self.name = name

    def add(self,component):
        pass

    def remove(self,component):
        pass

    def display(self):
        pass

class ConcreteComponent(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def display(self, depth=0):
        print "-"*depth+self.name
        for item in self.components:
            item.display(depth+2)

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def add(self, component):
        print "leaf cannot add components"

    def remove(self, component):
        print "leaf has no component"

    def display(self, depth=0):
        print "-"*depth+self.name


r = ConcreteComponent('root')
r.add(ConcreteComponent('A'))
r.add(ConcreteComponent('B'))
r.add(ConcreteComponent('C'))
r.components[0].add(ConcreteComponent('AA'))
r.components[1].add(ConcreteComponent('BA'))
r.components[2].add(ConcreteComponent('CA'))
r.components[0].components[0].add(ConcreteComponent('CA'))
r.components[2].add(Leaf('CC'))

r.display()

