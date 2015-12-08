#! /usr/bin/env python
# coding: utf-8


# 递归
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2 * f(n-2) + 3 * f(n-3)

for i in range(10):
    print f(i)


# 迭代
def g(n):
    if n < 3:
        return n
    else:
        a = 0
        b = 1
        c = 2
        for i in range(3, n+1):
            tmp = c + 2 * b + 3 * a
            a = b
            b = c
            c = tmp
    return c

for i in range(10):
    print g(i)
