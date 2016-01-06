#! /usr/bin/env python
import profile

number = 524287


def smallest_divisor(n):
    return find_divisor(n, 2)


def find_divisor(n, test_divisor):
    if test_divisor * test_divisor > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def test_smallest_divisor():
    for i in xrange(10000):
        smallest_divisor(number)


profile.run("test_smallest_divisor()")


def smallest_divisor_opt(n):
    return find_divisor_opt(n, 2)


def find_divisor_opt(n, test_divisor):
    if test_divisor * test_divisor > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor_opt(n, next(test_divisor))


def next(n):
    if n == 2:
        return 3
    else:
        return n + 2


def test_smallest_divisor_opt():
    for i in range(10000):
        smallest_divisor_opt(number)


profile.run("test_smallest_divisor_opt()")

"""
         7250004 function calls (20004 primitive calls) in 25.945 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
7240000/10000   25.891    0.000   25.891    0.003 1_23.py:11(find_divisor)
        1    0.018    0.018   25.945   25.945 1_23.py:20(test_smallest_divisor)
    10000    0.035    0.000   25.926    0.003 1_23.py:7(smallest_divisor)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000   25.945   25.945 <string>:1(<module>)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000   25.945   25.945 profile:0(test_smallest_divisor())


         7260005 function calls (3640005 primitive calls) in 24.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.033    0.000   23.995    0.002 1_23.py:28(smallest_divisor_opt)
3630000/10000   18.243    0.000   23.962    0.002 1_23.py:32(find_divisor_opt)
  3620000    5.719    0.000    5.719    0.000 1_23.py:41(next)
        1    0.019    0.019   24.014   24.014 1_23.py:48(test_smallest_divisor_opt)
        1    0.000    0.000    0.000    0.000 :0(range)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000   24.014   24.014 <string>:1(<module>)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000   24.014   24.014 profile:0(test_smallest_divisor_opt())
"""
# 优化后的速度并未使运行时间减少一半，两个速度的比值大约是1:1
# 因为相较于优化前的多一倍的find_divisor, 优化后减少了一半find_divisor过程
# 但增加了相同数量的next操作，猜测乘法和求余操作目前对cpu的消耗是等同的
# 因此出现速度上没有明显优势
