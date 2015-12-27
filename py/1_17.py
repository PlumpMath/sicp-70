#! /usr/bin/env python
# coding: utf-8


def multi(a, b):
    if b == 0:
        return 0
    else:
        return a + multi(a, b-1)


print multi(5, 8)


def double(a):
    return a * 2


def halve(b):
    return b / 2


def fast_multi(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return fast_multi(double(a), halve(b))
    else:
        return a + fast_multi(a, b-1)


print fast_multi(5, 8)
