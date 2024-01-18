"""
This is similar to the count_pairs_same_difference.py
"""
from collections import Counter


def count_substrings_anagrams(s):
    ctr = Counter()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sl = tuple(sorted(s[i:j]))
            ctr[sl] = ctr.get(sl, 0) + 1

    result = 0
    for k, v in ctr.items():
        result += (v * (v - 1)) // 2
    return result


if __name__ == "__main__":
    string = "ifailuhkqq"
    """ (i, i) (q, q), (ifa, fai) at - [0] [3] [8] [9] [0, 1, 2] [1, 2, 3] """
    result = count_substrings_anagrams(string)
    print(result)
