"""
Check if 2 strings are anagrams of each other
"""

from collections import Counter


def check_anagrams(str1, str2):
    ctr1 = Counter(str1)
    ctr2 = Counter(str2)
    return ctr1 == ctr2


def check_anagrams_version2(str1, str2):
    hmap1 = [0] * 26
    hmap2 = [0] * 26

    for char in str1:
        pos = ord(char) - ord("a")
        hmap1[pos] += 1

    for char in str2:
        pos = ord(char) - ord("a")
        hmap2[pos] += 1

    return hmap1 == hmap2


if __name__ == "__main__":
    str1 = "apple"
    str2 = "pleap"
    op = check_anagrams(str1, str2)
    print(op)
