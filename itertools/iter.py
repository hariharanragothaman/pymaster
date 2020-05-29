import itertools

# To flatten a nested list:
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flt = list(itertools.chain.from_iterable((list1)))
print(flt)
