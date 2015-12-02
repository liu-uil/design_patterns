#!/usr/bin/env python
# encoding: utf-8

class Mediator:
    def send(self, message, colleague):
        pass

class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator


class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleagueA = None
        self.colleagueB = None

    def send(self, message, colleague):
        if colleague == self.colleagueA:
            self.colleagueB.notify(message)

        elif colleague == self.colleagueB:
            self.colleagueA.notify(message)

        else:
            print "colleague is not belong to me"

class ConcreteColleagueA(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print "%s reveive the message %s"%(self.__class__, message)

class ConcreteColleagueB(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print "%s reveive the message %s"%(self.__class__, message)

m = ConcreteMediator()
c1 = ConcreteColleagueA(m)
m.colleagueA = c1
c2 = ConcreteColleagueB(m)
m.colleagueB = c2

c1.send('---this is c1---')
c2.send('---this is c2---')
