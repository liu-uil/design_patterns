#!/usr/bin/env python
# encoding: utf-8

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update()


class Observer:
    def update(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        state = ''

    def getState(self):
        return state

    def setState(self, value):
        self.state = value
        self.notify()


class ConcreteObserver(Observer):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.state = ''

    def update(self):
        self.state = self.subject.state
        print "observer %s state is %s "%(self.name, self.state)

    def getSubject(self):
        return self.subject

    def getSubject(self, subject):
        self.subject = subject

s = ConcreteSubject()
s.attach(ConcreteObserver(1,s))
s.attach(ConcreteObserver(2,s))
s.attach(ConcreteObserver(3,s))

s.setState('this is a new state')

