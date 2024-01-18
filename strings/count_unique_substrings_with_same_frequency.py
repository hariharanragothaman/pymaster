"""
Given a digit string s, return the number of unique substrings of s
where every digit appears the same number of times.

Reference: https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/
"""
from collections import *


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n, s_set = len(s), set()
        PRIME, MOD = 11, int(1e9 + 7)

        """
        1. Like how we do nested for loop - to generate all substrings, do the same thing
        2. But we need to do a few things smartly.
        3. Here we are updating a Counter as we are collecting substrings from a starting point.
        4. As we are collecting, let's count the max_cnt of each digit, 
            and we would know how many  distinct numbers we collected, as it's the length of the key of dict
        5. Now let's do max_cnt in dict * unique elemnts == right - left + 1
        6. To store the substrings, we use that math -hash to store them, instead of slicing and complicating
        
        
        """

        for left in range(n):
            cnt = Counter()
            max_cnt, s_hash = 0, 0

            for right in range(left, n):
                digit = ord(s[right]) - ord("0")
                cnt[digit] += 1
                max_cnt = max(max_cnt, cnt[digit])
                s_hash = (s_hash * PRIME + digit + 1) % MOD  # update hash in O(1)
                kcnt = len(cnt.keys())
                if max_cnt * kcnt == right - left + 1:
                    s_set.add(s_hash)
        return len(s_set)
