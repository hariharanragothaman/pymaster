"""
Given a limit, find how many numbers have the following:
- sum of their digits is equal to the number:
1 - 10, 100, 1000
2 - 2, 11
3 - 3, 12

So given 'n' find maximum number of numbers have this property

"""

from collections import defaultdict


def sum_of_digits(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    return total


g = defaultdict(int)
n = 12
for i in range(1, n + 1):
    g[sum_of_digits(i)] += 1
print(g)

res = 0
mx = max(g.values())
for k, v in g.items():
    if v == mx:
        res += 1

print(res)
