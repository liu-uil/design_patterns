#!/usr/bin/env python
# encoding: utf-8

class Strategy:
    def algorithm_interface(self):
        pass

class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print "algorithm A"

class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print "algorithm B"

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def ContextInterface(self):
        self.strategy.algorithm_interface()


c = Context(ConcreteStrategyA())
c.ContextInterface()

c.strategy = ConcreteStrategyB()
c.ContextInterface()
