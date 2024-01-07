"""
    How to check if 2 numbers are co-prime?
    2 numbers are said to be co-prime if the GCD of them is 1
"""
from math import gcd

def is_coprime(a, b) -> bool:
    return gcd(a, b) == 1
