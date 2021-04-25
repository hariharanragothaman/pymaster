import itertools
import operator

# To flatten a nested list:
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flt = list(itertools.chain.from_iterable((list1)))
print(flt)

# To consecutively multiply elements
arr = [1, 2, 3, 4, 5, 6]
op = list(itertools.accumulate(arr, operator.mul))
print(op)

# zipping unequal lists
a = [1, 2, 3]
b = [4, 5]
c = list(itertools.zip_longest(a, b, fillvalue=0))
print(c)