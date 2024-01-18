# GCD and LCM of b/w 2 numbers
from functools import reduce


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


# using reduce to find gcd for all multiple numbers at the same time. - you can also pass lambda to it.
from math import gcd

reduce(gcd, [2, 4, 8], 3)
