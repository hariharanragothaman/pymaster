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
def neighbours(r, c):
    for rows, cols in ((r - 1, c),
                       (r, c - 1),
                       (r + 1, c),
                       (r, c + 1)
                       ):
        if 0 <= rows < R and 0 <= cols < C:
            yield rows, cols


# Another way to write directions is:
i, j = 0, 0  # Assuming this is the start position
dirs = ((0,1),(0,-1),(1,0),(-1,0))
for x, y in dirs:
    row = i + x
    cols = j + y

# *****************************
# All diagonal elements have common difference between (i and j)
# Getting all all the diagonal elements
A = [[1, 2, 3], [4, 5 ,6], [7, 8, 9]]
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

# zipping unequal lists
a = [1, 2, 3]
b = [4, 5]
c = list(itertools.zip_longest(a, b, fillvalue=0))
print(c)