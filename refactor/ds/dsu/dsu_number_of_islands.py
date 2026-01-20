"""
Given a 2d grid map of '1's (land) and '0's (water),count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3

"""
from typing import List


class DisjointSetUnion:
    def __init__(self, n, num_sets):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = num_sets

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])

        edges = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    edges += 1
        dsu_obj = DisjointSetUnion(R * C, edges)

        def neighbours(r, c):
            for rows, cols in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= rows < R and 0 <= cols < C:
                    yield rows, cols

        for r, rows in enumerate(grid):
            for c, val in enumerate(rows):

                if grid[r][c] == "0":
                    continue

                # Math magic to make 2D matrix into 1D form and have them as edges.
                idx = r * C + c

                for nei in neighbours(r, c):
                    nr, nc = nei
                    if grid[nr][nc] == "1":

                        _idx = nr * C + nc
                        dsu_obj.union(idx, _idx)

        print(dsu_obj.num_sets)
        return dsu_obj.num_sets


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    islands = s.numIslands(grid)
    print(f"The number of islands are:", islands)
