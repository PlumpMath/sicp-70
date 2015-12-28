#! /usr/bin/env python
from datetime import datetime as dt


def timed_prime_test(n):
    if start_prime_test(n, dt.now()):
        return True


def start_prime_test(n, start_time):
    if prime(n):
        print n
        report_prime(dt.now() - start_time)
        return True


def report_prime(elapsed_time):
    print " *** "
    print elapsed_time


def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True


for i in [1000, 10000, 100000, 1000000]:
    n = 0
    while n < 3:
        i += 1
        if timed_prime_test(i):
            n += 1


# statistics: 素数检查耗时时间大约是10的开方倍数，略小，不到3
# 时间和步数大致正比
