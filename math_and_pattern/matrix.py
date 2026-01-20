from collections import defaultdict

def transpose_in_place(A) -> None:
    A[:] = [list(row) for row in zip(*A)]

def rotate_clockwise_in_place(A) -> None:
    """Rotate a matrix 90 degrees clockwise in-place."""
    A[:] = [list(row) for row in zip(*A[::-1])]

def rows(A):
    return [list(r) for r in A]

def columns(A):
    """Return the columns as lists (materialized)."""
    return [list(col) for col in zip(*A)]

def neighbors(r, c, R, C):
    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc

def get_left_diagonals(A):
    R = len(A)
    hashmap = {}
    for i in range(R):
        hashmap[(i, i)] = A[i][i]
    return hashmap

def get_right_diagonals(A):
    # R = len(arr)
    # i+j == R - 1
    R = len(A)
    hashmap = {}
    for i in range(R):
        hashmap[(R - 1 - i, i)] = A[R - 1 - i][i]
    return hashmap

def get_middle_row(A):
    # if n is odd
    R = len(A)
    mid = R // 2
    hashmap = {}
    for i in range(R):
        hashmap[(mid, i)] = A[mid][i]
    return hashmap

def get_middle_column(A):
    # if n is odd
    R = len(A)
    mid = R // 2
    hashmap = {}
    for i in range(R):
        hashmap[(i, mid)] = A[i][mid]
    return hashmap


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("Left diagonal:", get_left_diagonals(matrix))
    print("Right diagonal:", get_right_diagonals(matrix))
    print("Middle row:", get_middle_row(matrix))
    print("Middle column:", get_middle_column(matrix))
    rotate_clockwise_in_place(matrix)
    print("Rotated:", matrix)
