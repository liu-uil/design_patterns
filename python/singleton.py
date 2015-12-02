#!/usr/bin/env python
# encoding: utf-8

#第一种方法，用类的属性实现
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3

print one.a
print 'id is same?', one is two

#第二种方法，用修饰实现
def singleton(cls, *args, **kw):
    instance = {}
    def _singleton(*args, **kw):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton
class MyClass():
    def __init__(self, *args, **kw):
        for k,v in kw.items():
            print k,v

one = MyClass(2,a=1,b=2)
two = MyClass(4,c=3,d=4)


print one is two

