"""
https://leetcode.com/problems/path-with-maximum-minimum-value/

Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.
A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

"""

"""
Some general thoughts:
This is a beautiful question that TLE's on DFS and explains the need for Djikstra / using a heap
"""

from typing import List
from collections import deque


class Solution:
    def maximumMinimumPath(self, M: List[List[int]]) -> int:
        # So we need to find the max score of a path
        # the score in a path is the min(path)
        # So we are trying to maximize that min value
        # - The path is only as strong as it's smallest value

        R, C = len(M), len(M[0])

        def neighbours(r, c, R, C):
            for rows, cols in ((r - 1, c),
                               (r, c - 1),
                               (r + 1, c),
                               (r, c + 1)
                               ):
                if 0 <= rows < R and 0 <= cols < C:
                    yield rows, cols

        # Initializing the Q with start
        start = (0, 0)
        q = deque()
        q.append(start)

        # Initializing the path
        path = [M[0][0]]

        # Creating a visited mat
        visited = [[0] * C for i in range(R)]

        while q:
            i, j = q.pop()
            if (i, j) == (R - 1, C - 1):
                break

            visited[i][j] = 1
            max_value = 0
            max_r, max_c = 0, 0

            not_visited_nei = [(nr, nc) for nr, nc in neighbours(i, j, R, C) if not visited[nr][nc]]

            # I think the TLE is because of this
            for nr, nc in not_visited_nei:
                if M[nr][nc] > max_value:
                    max_value = M[nr][nc]
                    max_r, max_c = nr, nc
                visited[nr][nc] = 1

            q.append((max_r, max_c))
            path.append(max_value)

        return min(path)


if __name__ == '__main__':
    s = Solution()
    arr = [[5,4,5],[1,2,6],[7,4,6]]
    res = s.maximumMinimumPath(arr)
    print(res)