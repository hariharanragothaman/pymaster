# Find common characters in all strings in a list

from collections import Counter
from typing import List
from functools import reduce


class Solution:
    def commonChars(self, W: List[str]) -> List[str]:
        return reduce(lambda x, y: x & y, map(Counter, W)).elements()


class Solution2:
    def commonChars(self, W: List[str]) -> List[str]:
        n = len(W)
        H = Counter(W[0])
        for i in range(1, n):
            ctr = Counter(W[i])
            s1 = set(ctr.keys())
            s2 = set(H.keys())
            s3 = s1.intersection(s2)
            ctr2 = {}
            for c in s3:
                ctr2[c] = min(H[c], ctr[c])
            H = ctr2

        ans = []
        for k, v in H.items():
            ans += [k] * v
        return ans
