import math
import operator

from functools import reduce
from math import gcd

"""
# When you XOR, things will cancel out.
    print(6 ^ 6 ^ 6 ^ 10 ^ 10) -> 6
"""

class Math:
    @staticmethod
    def to_binary(n: int, padding: int = 0) -> str:
        bits = bin(n)[2:]  # remove '0b'
        return bits.zfill(padding)

    @staticmethod
    def factors(n) -> set:
        return set(reduce(list.__add__,([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0),))

    @staticmethod
    def n_c_r(self, n, r):
        nCr = lambda n, r: reduce(operator.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
        return nCr

    def catalan(self, n):
        return lambda n: self.n_c_r(2 * n, n) // (n + 1)

    @staticmethod
    def powers_of_two():
        pow2 = [1 << i for i in range(62)]
        return pow2

    @staticmethod
    def multiply_by_2(n):
        return n << 1

    @staticmethod
    def divide_by_2(n):
        return n >> 1

    @staticmethod
    def two_power_n(n):
        return 1 << n

    @staticmethod
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

    def hamming_distance(self, a, b):
        x = a ^ b
        dist = 0
        while x > 0:
            dist += x & 1
            x >>= 1
        return dist

if __name__ == '__main__':
    m = Math()
    result = m.to_binary(5, 5)
    print(result)

    f = m.factors(16)
    print(f)
