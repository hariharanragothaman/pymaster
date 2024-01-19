"""
Given two strings str1 and str2 of the same length
Determine whether you can transform str1 into str2 by doing zero or more conversions.
In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
Return true if and only if you can transform str1 into str2.
"""

from collections import Counter

def can_convert(s1, s2) -> bool:
    """Convert 2 strings of same length by doing zero or more conversions"""
    if s1 == s2:
        return True
    dp = {}
    for i, j in zip(s1, s2):
        if dp.setdefault(i, j) != j:
            return False
    return len(set(s2)) < 26

"""
Given 2 strings s1 and s2 - check if s2 can be formed from s1, no duplication allowed
-> Check if 1 hashmap is a subset of another hashmap
"""


def check_hashmap_subset(s1, s2) -> bool:
    # Check if s2 can be formed from s1
    ctr1 = Counter(s1)
    ctr2 = Counter(s2)

    if set(ctr1.keys()) & set(ctr2.keys()) == set():
        return False
    else:
        # Check for actual count
        for k, v in ctr2.items():
            if ctr1[k] < v:
                return False
        return True
