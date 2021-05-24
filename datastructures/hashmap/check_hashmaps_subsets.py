from typing import List
from collections import Counter

"""
Given 2 strings s1 and s2 - check if s2 can be formed from s1, no duplication allowed
-> Check if 1 hashmap is a subset of another hashmap
"""


def check_hashmap_subset(s1: List, s2: List) -> bool:
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
