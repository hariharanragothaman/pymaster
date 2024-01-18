from itertools import accumulate
import operator

A = [1, 2, 3, 4, 5]
ans = list(accumulate(A, operator.mul))
print(ans)
