import math
import operator
from functools import reduce


nCr = lambda n, r: reduce(operator.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
catalan = lambda n: nCr(2 * n, n) // (n + 1)
derangements = lambda n: int(math.factorial(n) / math.e + 0.5)
print(nCr(5, 2))
