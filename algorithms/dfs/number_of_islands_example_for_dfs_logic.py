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
from collections import deque

def number_of_islands(grid):
    if not grid:
        return 0

    islands = 0
    R = len(grid)
    C = len(grid[0])
    q = deque()

    # Helper function to get the neighbours
    def neighbours(r, c):
        for rows, cols in ((r - 1, c),
                           (r, c - 1),
                           (r + 1, c),
                           (r, c + 1)
                           ):
            if 0 <= rows < R and 0 <= cols < C:
                yield rows, cols

    def helper(grid, i, j):
        q.append((i, j))
        while q:
            r, c = q.popleft()
            for nei in neighbours(r, c):
                x, y = nei
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    q.append((x, y))

    # Core logic - find a 1 and marks it's neighbours as zero
    for r, rows in enumerate(grid):
        for c, val in enumerate(rows):
            if val == '1':
                grid[r][c] = '0'
                helper(grid, r, c)
                islands += 1
    return islands