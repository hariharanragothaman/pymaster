from functools import reduce
from math import gcd


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


# using reduce to find gcd for all multiple numbers at the same time. - you can also pass lambda to it.
reduce(gcd, [2, 4, 8], 3)
