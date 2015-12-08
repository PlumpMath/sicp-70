#! /usr/bin/env python
# coding: utf-8

p_number = 0


def cube(x):
    return x * x * x


def p(x):
    global p_number
    p_number += 1
    return 3 * x - 4 * cube(x)


def sine(x):
    if not abs(x) > 0.1:
        return x
    else:
        return p(sine(x / 3.0))


print sine(12.15)
print p_number
