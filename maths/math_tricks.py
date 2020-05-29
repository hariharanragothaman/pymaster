from functools import reduce


# To find all factors of a give number
def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


# 2D matrices Hacks
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[:] = zip(*matrix)  # Getting Transpose [ R->C, C->R ]
matrix[:] = zip(*matrix[::-1])  # Rotate a matrix - Transpose & reverse each row

# To get the rows of the matrix:
def get_rows(matrice):
    return [[c for c in r] for r in matrice]

def get_columns(matrice):
    return zip(*matrice)

