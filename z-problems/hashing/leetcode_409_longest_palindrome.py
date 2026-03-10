from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ctr = Counter(s)
        cnt = 0
        rem = ""
        for k, v in ctr.items():
            q, r = divmod(v, 2)
            cnt += q * 2
            rem += k * r
        if rem:
            cnt += 1
        return cnt
