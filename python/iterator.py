#!/usr/bin/env python
# encoding: utf-8

class Iterator:
    def first(self):
        pass

    def next(self):
        pass

    def isDone(self):
        pass

    def currentItem(self):
        pass


class Aggregate:
    def createIterator(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.current = 0
        self.aggregate = aggregate

    def first(self):
        return self.aggregate[0]

    def next(self):
        ret = None
        self.current += 1
        if self.current < self.aggregate.count():
            ret = self.aggregate[self.current]
        return ret

    def isDone(self):
        return False if self.current < self.aggregate.count() else True

    def currentItem(self):
        return self.aggregate[self.current]


class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.items = []

    def createIterator(self):
        return ConcreteIterator(self)

    def insertValue(self, val, index = 0):
        self.items.insert(index, val)

    def __getitem__(self, index):
        return self.items[index]

    def count(self):
        return len(self.items)

a = ConcreteAggregate()
a.insertValue('one')
a.insertValue('two')
a.insertValue('three')
a.insertValue('four')
a.insertValue('five')

itr = a.createIterator()
f = itr.first()
while(not itr.isDone()):
    print itr.currentItem()
    itr.next()


