import math
import operator

from functools import reduce
from math import gcd
from itertools import chain, combinations

"""
# When you XOR, things will cancel out.
    print(6 ^ 6 ^ 6 ^ 10 ^ 10) -> 6
"""

def to_binary(n: int, padding: int = 0) -> str:
    bits = bin(n)[2:]  # remove '0b'
    return bits.zfill(padding)

def factors(n) -> set:
    return set(reduce(list.__add__,([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0),))

def n_c_r(n, r):
    nCr = lambda n, r: reduce(operator.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
    return nCr

def catalan(n):
    return lambda n: n_c_r(2 * n, n) // (n + 1)

def powers_of_two():
    pow2 = [1 << i for i in range(62)]
    return pow2

def multiply_by_2(n):
    return n << 1

def divide_by_2(n):
    return n >> 1

def two_power_n(n):
    return 1 << n

def count_bits_set_to_one(n) -> int:
    """
    x << y # Shift to left by y bits -- x * (2**y)
    x >> y  # Shift to right by y bits -- x // (2**y)
    Args:
        n: The I/P number
    Returns:
    Logic: And with 1 , and keep dividing n by powers of 2
    """
    num_bits = 0
    while n:
        num_bits += n & 1
        n = n >> 1
        print("n is:", n)
    return num_bits

def is_coprime(a, b) -> bool:
    return gcd(a, b) == 1

def hamming_distance(a, b):
    x = a ^ b
    dist = 0
    while x > 0:
        dist += x & 1
        x >>= 1
    return dist

def go_over_all_combinations(A):
    n = len(A)
    for mask in range(1 << n):
        subset = [A[i] for i in range(n) if mask & (1 << i)]
        print(subset)

def apple_division(A, n):
    total = sum(A)
    ans = float("inf")
    limit = 1 << n

    # Going through all the combinations generated
    for msk in range(limit):
        s = 0
        # Remember Length of the bit-array
        for j in range(0, n):
            # Check and get if the ith bit is set
            if msk & (1 << j):
                s += A[j]
            current_difference = abs((total - s) - s)
            ans = min(ans, current_difference)
    print(ans)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# using reduce to find gcd for all multiple numbers at the same time. - you can also pass lambda to it.
reduce(gcd, [2, 4, 8], 3)

def lcm(a, b):
    return a * b / gcd(a, b)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def to_base_k(self, n: int, k: int) -> str:
    res = []
    while n:
        n, rem = divmod(n, k)
        res.append(rem)
    res = res[::-1]
    res = ''.join(str(c) for c in res)
    return res


def x_pow_n_mod_m(x, n, m):
    if n == 0:
        return 1
    if n % 2 == 0:
        return x_pow_n_mod_m((x * x) % m, n // 2, m)
    return x * x_pow_n_mod_m(x, n - 1, m) % m

def compute_square_root(k):
    left, right = 0, k
    while left <= right:
        pivot = (left + right) // 2
        if pow(pivot, 2) <= k:
            left = pivot + 1
        else:
            right = pivot - 1
    return left - 1
