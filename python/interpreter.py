#!/usr/bin/env python
# encoding: utf-8

class AbstractExpression:
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        print "终端解释器"

class NonterminalExpression(AbstractExpression):
    def interpret(self, context):
        print "非终端解释器"

class Context:
    def __init__(self):
        self.input = None
        self.output = None

c = Context
iList = []
iList.append(TerminalExpression())
iList.append(NonterminalExpression())
iList.append(TerminalExpression())
iList.append(TerminalExpression())

for item in iList:
    item.interpret(c)
