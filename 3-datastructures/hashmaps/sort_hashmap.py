# Pattern to sort a hash-map by key or value
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}  # by value
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])}  # by key

# To sort by value and then by key
# Creates a tuple that are by default sorted by value, and then we set the priority
ctr = {}
hash_map = sorted(hash_map, key=lambda x: (-ctr[x], x))


"""
Always remember - when you want to set multiple priorities - you need to create a tuple
"""
# Consider the following
A = [(2, 2), (-1, 1), (1, 1)]
"""
1. Here by default it's the ascending order
2. We give max priority to x[1]
3. If x[1] is the same then we give priority to x[0], but the '-' sign indicates the reverse order
"""
A = sorted(A, key=lambda x: (x[1], -x[0]) )
