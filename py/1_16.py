#! /usr/bin/env python
# coding: utf-8


def expt(b, n):
    return expt_iter(b, n, 1)


def expt_iter(b, counter, product):
    if counter == 0:
        return product
    else:
        return expt_iter(b, counter-1, product * b)


def fast_expt(b, n):
    return fast_expt_iter(b, n, 1)


def fast_expt_iter(b, counter, product):
    if counter == 0:
        return product
    elif counter % 2 == 0:
        return fast_expt_iter(b * b, counter/2, product)
    else:
        return fast_expt_iter(b, counter-1, product * b)


expt(2, 30)
fast_expt(2, 30)
