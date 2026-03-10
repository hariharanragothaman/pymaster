# Container with Most Water

from typing import List
class Solution:
    def maxArea(self, H: List[int]) -> int:
        n = len(H)
        ans = 0
        l, r = 0, n-1
        max_area = (r-l) * min(H[r], H[l])

        while l < r:
            if H[l] < H[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, (r-l)*min(H[r], H[l]))

        return max_area
