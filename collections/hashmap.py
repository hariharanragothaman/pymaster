from collections import Counter, deque, defaultdict, OrderedDict

# Pattern to sort a hash-map by key or value
hash_map = {}
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}   # by value
hash_map = {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])}   # by key

# To sort by value and then by key
# Creates a tuple that are by default sorted by value, and then we set the priority
ctr = {}
hash_map = sorted(hash_map, key=lambda x:(-ctr[x], x))

# Getting the most-common elements from input
array = [1, 3, 5, 6, 7, 7, 1, 1, 2, 3]
a_ctr = Counter(array)
top_three_frequent = a_ctr.most_common(3)

# Power of default-dictionary
d = defaultdict(list)
d['python'].append("awesome")     # No-need to check if key exists
d['something-else'].append("not relevant")
d['python'].append("language")
print(d)
