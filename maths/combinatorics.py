import math
import operator
from functools import reduce


nCr = lambda n, r: reduce(operator.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)
print(nCr(5, 2))