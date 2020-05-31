"""
There are totally 4 recipes for binary search
1. The regular usual one
2.
3.
4. Using bisect
"""

# TEMPLATE #4 - Bisect and its advantages

from bisect import bisect_left, bisect_right


def binary_search(array, value):
    index = bisect_left(array, value)
    if index != len(array) and array[index] == value:
        return index
    else:
        return -1


arr = [1, 2, 4, 4, 5, 6, 7]
value = 4
res = binary_search(arr, 7)
print(res)
