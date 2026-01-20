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
