# Count pairs less than target

from typing import List

class Solution:
    def countPairs(self, A: List[int], T: int) -> int:
        n = len(A)
        cnt = 0
        A.sort()
        print(A)

        l, r = 0, n-1
        while l < r:
            if A[l] + A[r] < T:
                cnt += r - l
                l += 1
            else:
                r -= 1
        return cnt
