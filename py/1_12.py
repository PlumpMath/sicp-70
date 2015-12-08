#! /usr/bin/env python
# coding: utf-8


# n present the layer number
def triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        return generate(triangle(n-1))


def generate(l):
    new_l = []
    new_l.append(l[0])
    for i in range(len(l)-1):
        new_l.append(l[i] + l[i+1])
    new_l.append(l[-1])
    return new_l


for i in range(1, 6):
    print triangle(i)
