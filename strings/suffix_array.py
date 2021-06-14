from collections import defaultdict
from itertools import zip_longest, islice

"""
Let s be a string of length n
The ith suffix of s is the sub-string s [i..n-1]

The suffix array will contain integers that represent the starting index of the all the suffixes

s = "abaab"

All the suffixes are:
 0 - abaab
 1 - baab
 2 - aab
 3 - ab
 4 - b

 After sorting them

 2 - aab
 3 - ab
 0 - abaab
 4 - b
 1 - baab

 Suffix array will be - (2, 3, 0, 4, 1)

 Things covered:
 1. Construction of a Suffix array
 2. Applications
"""

from misc.time_decorator import timeit

def build_suffix_array_naive(s):
    """ n**2 (log(n))"""
    suffixes = []
    for i in range(len(s)):
        suffixes.append(s[i:])
    print("The suffixes are:", suffixes)
    hmap = defaultdict(int)
    for i, c in enumerate(suffixes):
        hmap[c] = i
    print("The hashmap is:", hmap)
    sorted_suffixes = sorted(suffixes)
    print(sorted_suffixes)

    sufffix_array_result = []
    for c in sorted_suffixes:
        sufffix_array_result.append(hmap[c])
    return sufffix_array_result

@timeit
def build_suffix_array_naive_better(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

if __name__ == '__main__':
    s = "abaab"
    suffix_array = build_suffix_array_naive_better(s)
    print(suffix_array)