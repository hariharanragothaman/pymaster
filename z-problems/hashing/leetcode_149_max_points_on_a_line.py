from typing import List
from collections import defaultdict

"""
Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
"""


class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        print(A)
        n = len(A)

        if n <= 2:
            return n

        A = [tuple(c) for c in A]
        mx = 0

        for i in range(n):
            H = defaultdict(set)
            for j in range(i+1, n):
                x1, y1 = A[i]
                x2, y2 = A[j]
                num = y2 - y1
                deno = x2 - x1

                if  deno != 0:
                    slope = (y2-y1) / (x2-x1)
                else:
                    slope = float('inf')

                H[slope].add((x1, y1))
                H[slope].add((x2, y2))

            for k, v in H.items():
                mx = max(mx, len(v))
        return mx