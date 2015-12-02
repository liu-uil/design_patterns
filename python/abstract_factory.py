#!/usr/bin/env python
# encoding: utf-8

class Base():
    def __init__(self):
        print "this is the base"

    def operation(self):
        pass

class ConstantA(Base):
    def __init__(self):
        Base.__init__(self)
        print "this is the ConstantA"

    def operation(self):
        print "this is A's operation"

class ProductAA(ConstantA):
    def __init__(self):
        ConstantA.__init__(self)
        print "this is Product AA"

    def operation(self):
        print "this is Product AA's operation"

class ProductAB(ConstantA):
    def __init__(self):
        ConstantA.__init__(self)
        print "this is Product AB"

    def operation(self):
        print "this is Product AB's operation"

class ConstantB(Base):
    def __init__(self):
        Base.__init__(self)
        print "this is the ConstantB"

    def operation(self):
        print "this is B's operation"


class ProductBA(ConstantB):
    def __init__(self):
        ConstantB.__init__(self)
        print "this is Product BA"

    def operation(self):
        print "this is Product BA's operation"

class ProductBB(ConstantB):
    def __init__(self):
        ConstantB.__init__(self)
        print "this is Product BB"

    def operation(self):
        print "this is Product BB's operation"

class FactoryBase:
    def  __init__(self):
        print "this is the FactoryBase"

    @staticmethod
    def create():
        pass

class FactoryA(FactoryBase):
    @staticmethod
    def createA():
        instance = ProductAA()
        return instance
    @staticmethod
    def createB():
        instance = ProductAB()
        return instance

class FactoryB(FactoryBase):
    @staticmethod
    def createA():
        instance = ProductBA()
        return instance
    @staticmethod
    def createB():
        instance = ProductBB()
        return instance

#此处如果要换产品线只需将FactoryA替换，但是如果程序中多次用到FactroyA，会需要多次操作
factory = FactoryA
o1 = factory.createA()
o1.operation()
o2 = factory.createB()
o2.operation()

#简单工厂方法对抽象工厂改进
class SimpleImprove:
    #如果要换产品线，只需要将'A'替换
    opt = 'A'
    @staticmethod
    def createA():
        if SimpleImprove.opt == 'A':
            instance = FactoryA.createA()
        elif SimpleImprove.opt == 'B':
            instance = FactoryB.createA()
        return instance

    @staticmethod
    def createB():
        if SimpleImprove.opt == 'A':
            instance = FactoryA.createB()
        elif SimpleImprove.opt == 'B':
            instance = FactoryB.createB()
        return instance


o1 = SimpleImprove.createA()
o1.operation()
o2 = SimpleImprove.createB()
o2.operation()

#用反射改进
opt = 'A'

class FactoryCommon:
    @staticmethod
    def createA():
        fooName = 'Factory'+opt
        instance = eval(fooName).createA()
        return instance

    @staticmethod
    def createB():
        fooName = 'Factory'+opt
        instance = eval(fooName).createB()
        return instance


o1 = FactoryCommon.createA()
o1.operation()
o2 = FactoryCommon.createB()
o2.operation()
