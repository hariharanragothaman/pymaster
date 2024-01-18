import collections
from typing import Any


def transpose(A):
    """Getting Transpose [ R->C, C->R ]"""
    A[:] = zip(*A)
    return A


def rotate_matrix(A):
    """Rotate a matrix - Transpose & reverse each row"""
    A[:] = zip(*A[::-1])
    return A


def get_rows(A) -> list:
    """Return the rows of the matrix"""
    return [[c for c in r] for r in A]


def get_columns(A) -> list:
    """Return the cols of the matrix"""
    return zip(*A)


def neighbours(r, c, R, C):
    """Return the neighbours of a matrix element"""
    for rows, cols in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
        if 0 <= rows < R and 0 <= cols < C:
            yield rows, cols


def get_neighbours_alternate(r, c, R, C):
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for x, y in dirs:
        row = r + x
        col = c + y
        if 0 <= row < R and 0 <= col < C:
            yield row, col


# *****************************
# All diagonal elements have common difference between (i and j)
# Getting all the diagonal elements
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n, m = 3, 3
d = collections.defaultdict(list)
for i in range(n):
    for j in range(m):
        d[i - j].append(A[i][j])

# Putting them back
for i in range(n):
    for j in range(m):
        A[i][j] = d[i - j].pop()

# *******************************
# Getting the diagonals


def get_right_diagonals(A) -> dict[tuple[int, int], Any]:
    # R = len(arr)
    # i+j == R - 1
    rows = len(A)
    hashmap = {}
    for i in range(rows):
        hashmap[(rows - 1 - i, i)] = A[rows - 1 - i][i]
    return hashmap


def get_left_diagonals(A):
    rows = len(A)
    hashmap = {}
    for i in range(rows):
        hashmap[(i, i)] = A[i][i]
    return hashmap

def get_middle_row(A):
    # if n is odd
    rows = len(A)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(mid, i)] = A[mid][i]
    return hashmap


def get_middle_column(A):
    # if n is odd
    rows = len(A)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(i, mid)] = A[i][mid]
    return hashmap


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
