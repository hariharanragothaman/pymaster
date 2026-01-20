import math
import operator

from functools import reduce
from math import gcd

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


if __name__ == '__main__':
    m = Math()
    result = m.to_binary(5, 5)
    print(result)
