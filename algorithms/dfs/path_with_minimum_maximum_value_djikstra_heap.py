from typing import List
from heapq import heappush, heappop


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
        q = []
        q.append((-M[0][0], 0, 0))

        print("The queue is:", q)

        # Creating a visited mat
        visited = [[0] * C for i in range(R)]

        while q:
            cost, i, j = heappop(q)
        
            # minimum across -ve's will give you the maximum - Hahah. This is so philospohical.
            cost = -cost

            if (i, j) == (R - 1, C - 1):
                return cost

            # This is something we forgot
            if visited[i][j]:
                continue

            visited[i][j] = 1

            not_visited_nei = [(nr, nc) for nr, nc in neighbours(i, j, R, C) if not visited[nr][nc]]

            # I think the TLE is because of this
            for nr, nc in not_visited_nei:
                # This line is just being smart in terms of memory saving.
                heappush(q, (-min(cost, M[nr][nc]), nr, nc))

        return 0