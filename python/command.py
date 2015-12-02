#!/usr/bin/env python
# encoding: utf-8

class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self.receiver.action()

class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

class Receiver:
    def action(self):
        print "this is receiver action"


r = Receiver()

c = ConcreteCommand(r)
i = Invoker()
i.set_command(c)
i.execute_command()
