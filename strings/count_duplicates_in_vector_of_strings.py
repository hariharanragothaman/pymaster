from typing import List
from collections import defaultdict


def compute_hash(s):
    p = 31
    m = 10**9 + 9
    hash_value = 0
    pow = 1

    for c in s:
        hash_value = (hash_value + (ord(c) - ord("a") + 1) * pow) % m
        pow = (pow * p) % m
    return hash_value


def group_identical_strings(arr: List[str]):
    hashes = []
    result_groups = defaultdict(list)

    # Computing the hashes of all strings
    for i, s in enumerate(arr):
        hashes.append((compute_hash(s), i))
    print(hashes)

    # Sorting the hashes: -> Basically converting strings to integers
    hashes = sorted(hashes)
    print("Hashes after sorting", hashes)

    for h in hashes:
        result_groups[h[0]].append(h[1])

    print("The map is:", result_groups)
    print("The result groups are:", result_groups.values())


if __name__ == "__main__":
    arr = ["abc", "abc", "defgh", "codeforces", "leetcode", "hello", "world", "hello"]
    group_identical_strings(arr)
