from typing import List
from heapq import heappop, heappush

# This problem can be also be a Djikstra template

"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). 
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) 
(i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

"""


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # This is a question classically designed for Djikstra
        # Now, we can do DFS and DJikstra

        R, C = len(heights), len(heights[0])

        def neighbours(r, c, R, C):
            for rows, cols in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= rows < R and 0 <= cols < C:
                    yield rows, cols

        # Travelling from destination to source
        q = [(0, R - 1, C - 1)]
        # print(q)

        visited = [[0] * C for i in range(R)]
        # print(visited)

        """
        1. Each path's weight is the difference of consecutive nodes
        2. For the overall effort to be minimum, we need to choose the smallest diff path - This heappop and heappush - djikstra
        3. We need to take the maxiumum value in that and return it
        """

        min_cost = []

        while q:
            node = heappop(q)
            value, x, y = node
            # print("The chosen value is:", node)

            min_cost.append(value)

            # Reached the end
            if (x, y) == (0, 0):
                return max(min_cost)

            if visited[x][y]:
                continue

            visited[x][y] = 1

            # Getting the not visited neighbours
            not_visited_nei = [
                (nr, nc) for nr, nc in neighbours(x, y, R, C) if not visited[nr][nc]
            ]

            for nr, nc in not_visited_nei:
                heappush(q, (abs(heights[nr][nc] - heights[x][y]), nr, nc))

            # print("The queue is:", q)
            # print("*************************************")

        # print("The min_cost is:", min_cost)
        return 0
