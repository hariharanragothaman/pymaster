from typing import List
from collections import Counter, deque, defaultdict, OrderedDict

# Pattern to sort a hash-map by key or value
hash_map = {}
hash_map = {
    k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])
}  # by value
hash_map = {
    k: v for k, v in sorted(hash_map.items(), key=lambda item: item[0])
}  # by key

# Classic example of sort by value and then by key
# Here -ve sign signifies that you want to order values in reverse - 1st priority
# then the key - which is second priority
class Solution:
    def topKFrequentWords(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        result = sorted(ctr, key=lambda x: (-ctr[x], x))
        return result[:k]


# To sort by value and then by key
# Creates a tuple that are by default sorted by value, and then we set the priority
ctr = {}
hash_map = sorted(hash_map, key=lambda x: (-ctr[x], x))

# Getting the most-common elements from input
array = [1, 3, 5, 6, 7, 7, 1, 1, 2, 3]
a_ctr = Counter(array)
top_three_frequent = a_ctr.most_common(3)

# Power of default-dictionary
d = defaultdict(list)
d["python"].append("awesome")  # No-need to check if key exists
d["something-else"].append("not relevant")
d["python"].append("language")
print(d)

# Setdefault feature example
# String transforms to another string problem?
def can_convert(s1, s2):
    """Convert 2 strings of same length by doing zero or more conversions"""
    if s1 == s2:
        return True
    dp = {}
    for i, j in zip(s1, s2):
        if dp.setdefault(i, j) != j:
            return False
    return len(set(s2)) < 26
