#!/usr/bin/env python
# encoding: utf-8

class Originator:
    def __init__(self):
        self.state = 100

    def create_memo(self):
        return Memo(self.state)

    def set_memo(self, memo):
        self.state = memo.state

    def show(self):
        print "state is ", self.state

class Memo:
    def __init__(self, state):
        self.state = state

#例子比较简单，所以CareTaker的作用不明显，但是如果要保存多个状态，CareTaker的管理作用就体现出来了
class CareTaker:
    def __init__(self):
        self.memo = None

c = CareTaker()

o = Originator()
o.show()
o.state = 70
o.show()
c.memo = o.create_memo()

o.state = 30
o.show()
o.set_memo(c.memo)
o.show()
