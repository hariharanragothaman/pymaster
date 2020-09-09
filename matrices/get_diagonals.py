# Storing the left diagonals in a hashmap
for i in range(rows):
    hashmap[(i, i)] = mat[i][i]

# Storing the right diagonals in a hashmap
for i in range(rows):
    hashmap[(rows - 1 - i, i)] = mat[rows - 1 - i][i]
