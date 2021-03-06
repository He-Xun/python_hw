# -*- coding:utf-8 -*-
from collections import Iterable
import functools

def fn(x):
    return x * x

def map1(func, iterable):
    if not callable(func):
        raise Exception('func is not callable')
    if not isinstance(iterable, (Iterable)):
        raise Exception('Iterable is not Iterabel')
    else:
        return (func(value) for index, value in enumerate(iterable))


ret = list(map1(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(ret)

print('------------------')

def fn(x, y):
    return x + y

def reduce1(func, iterable, initval=0):
    if not callable(func):
        raise Exception('func is not callable')
    if not isinstance(iterable, (Iterable)):
        raise Exception('Iterable is not Iterabel')

    if isinstance(iterable,(str)):
        return iterable
    else:
        l = iterable
        while True:
            if len(l) >= 2:
                l[0] = func(l[0], l[1])
                l.pop(1)
            else:
                return func(l[0], initval)

ret = reduce1(fn, [1, 3, 5, 7, 9], 100)
ret1 = functools.reduce(fn, [1, 3, 5, 7, 9], 100)
ret2 = reduce1(fn, '1234')
ret3 = functools.reduce(fn,'1234')

print(ret)
print(ret1)
print(ret2)
print(ret3)

print('------------------')


def fn(n):
    return n % 2 == 1

print('------------------')

def fn(n):
    return n % 2 == 1

def filter1(func, iterable):
    if not callable(func):
        raise Exception('func is not callable')
    if not isinstance(iterable, (Iterable)):
        raise Exception('Iterable is not Iterabel')
    else:
        cplst = []
        for x in iterable:
            if fn(x):
                cplst.append(x)
        else:
            return cplst

ret = list(filter1(fn, [1, 2, 4, 5, 6, 9, 10, 15]))
print(ret)
