# -*- coding: utf-8 -*-

class pyaop(type):

    def nop(self):
        pass

    beforeop = nop
    afterop = nop

    @classmethod
    def setbefore(mcs, func):
        pyaop.beforeop = func

    @classmethod
    def setafter(mcs, func):
        pyaop.afterop = func

    def __new__(mcl, name, bases, dict):
        from types import FunctionType  # 加载类型模块的FunctionType
        obj = object()  # 定义一个空对象的变量

        def aop(func):

            def wrapper(*args, **kwds):
               pyaop.beforeop(obj)  # 调用前置函数
               value = func(*args, **kwds)
               pyaop.afterop(obj)  # 调用后置函数
               return value

            return wrapper

        for attr, value in dict.iteritems():
            if isinstance(value, FunctionType):
                dict[attr] = aop(value)  # 找到后用aop这个函数替换之

        obj = super(pyaop, mcl).__new__(mcl, name, bases, dict)  # 调用父类的__new__()创建self

        return obj

class TestCls(object):
    __metaclass__ = pyaop
    c = 2

    @classmethod
    def sss(cls):
        print 'kkk', cls.c

    def ttt(self):
        print 'hello'


def befn(self):
    print 'before:',

def affn(self):
    print 'end'

pyaop.setbefore(befn)
pyaop.setafter(affn)

a = TestCls()
b = TestCls()

b.c = 3

a.ttt()
print a.c, TestCls.c, b.c

b.sss()
TestCls.sss()