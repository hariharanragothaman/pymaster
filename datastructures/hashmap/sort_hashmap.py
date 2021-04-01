# Pattern to sort a hash-map by key or value
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}   # by value
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])}   # by key

# To sort by value and then by key
# Creates a tuple that are by default sorted by value, and then we set the priority
ctr = {}
hash_map = sorted(hash_map, key=lambda x:(-ctr[x], x))