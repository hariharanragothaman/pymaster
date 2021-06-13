import itertools
import collections

# 2D matrices Hacks
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Getting Transpose [ R->C, C->R ]
matrix[:] = zip(*matrix)

# Rotate a matrix - Transpose & reverse each row
matrix[:] = zip(*matrix[::-1])

# To get the rows of the matrix:
def get_rows(matrice):
    return [[c for c in r] for r in matrice]


# To the cols of the matrix
def get_columns(matrice):
    return zip(*matrice)


# To get the neighbours of a matrix element
def neighbours(r, c, R, C):
    for rows, cols in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
        if 0 <= rows < R and 0 <= cols < C:
            yield rows, cols


# Another way to write directions is:
i, j = 0, 0  # Assuming this is the start position
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
for x, y in dirs:
    row = i + x
    cols = j + y

# *****************************
# All diagonal elements have common difference between (i and j)
# Getting all all the diagonal elements
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

def get_right_diagonals(arr):
    rows = len(arr)
    hashmap = {}
    for i in range(rows):
        hashmap[(rows-1-i, i)] = arr[rows-1-i][i]
    return hashmap

def get_left_diagonals(arr):
    rows = len(arr)
    hashmap = {}
    for i in range(rows):
        hashmap[(i, i)] = arr[i][i]
    return hashmap

def get_middle_row(arr):
    # if n is odd
    rows = len(arr)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(mid, i)] = arr[mid][i]
    return hashmap

def get_middle_column(arr):
    # if n is odd
    rows = len(arr)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(i, mid)] = arr[i][mid]
    return hashmap