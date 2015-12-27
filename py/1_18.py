#! /usr/bin/env python
# coding: utf-8


def double(a):
    return a * 2


def halve(b):
    return b / 2


def fast_multi(a, b):
    return fast_multi_iter(a, b, 0)


def fast_multi_iter(a, counter, product):
    if counter == 0:
        return product
    elif counter % 2 == 0:
        return fast_multi_iter(double(a), halve(counter), product)
    else:
        return fast_multi_iter(a, counter-1, product + a)


print fast_multi(5, 8)
