"""
Given a string, we need to find , if it contains AB, and BA seperately and they are non-overlapping
The strings can be in any order.
"""
from typing import List

p = 31
m = 10 ** 9 + 9


def compute_hash(s):
    n = len(s)

    power_mod = [1]
    for i in range(n):
        power_mod.append((power_mod[-1] * p) % m)

    hash_values = [0] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (
            hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]
        ) % m


def count_occurences(text, pattern):
    """
    :param pattern: Pattern Text
    :param text: I/P text
    :return:
    """
    text_length = len(text)
    pattern_length = len(pattern)

    power_mod = [1]
    for i in range(text_length):
        power_mod.append((power_mod[-1] * p) % m)
    # print(f"The power mod is: {[power_mod]}")

    hash_values = [0] * (text_length + 1)

    for i in range(text_length):
        hash_values[i + 1] = (
            hash_values[i] + (ord(text[i]) - ord("a") + 1) * power_mod[i]
        ) % m
    # print("The string hash values are:", hash_values)

    pattern_hash = 0
    for i in range(pattern_length):
        pattern_hash += ((ord(pattern[i]) - ord("a") + 1) * power_mod[i]) % m
    # print("The pattern hash is:", pattern_hash)

    occurences = []

    i = 0
    while i + pattern_length - 1 < text_length:
        field_hash = (hash_values[i + pattern_length] - hash_values[i] + m) % m
        if field_hash == pattern_hash * power_mod[i] % m:
            occurences.append(i)
        i += 1

    return occurences


def solve(s):
    """
    AB and BA are defined strings of length 2
    We can do rabin-karp, to get this.
    So find where all AB is - ab_result
    find where all BA is - ba_result
    AB, BA occurence - ensure it's not overalling
    :return:
    """
    # Let's try a bruteforce method first - This will TLE
    def helper(s, char) -> List:
        n = len(s)
        res = []
        start = 0
        while s:
            idx = s.find(char, start, n)
            if idx != -1:
                res.append(idx)
                start += 2
            elif idx == -1:
                break
        return res

    # result1 = helper(s, char='AB')
    # result2 = helper(s, char='BA')

    result1 = count_occurences(s, pattern="AB")
    result2 = count_occurences(s, pattern="BA")

    # We now have to basically find if we can find 2 non-overalapping intervals

    a = []
    b = []

    if result1 and result2:
        if result1[0] < result2[0]:
            a, b = result1, result2
        else:
            a, b = result2, result1

        for i, val1 in enumerate(a):
            for j, val2 in enumerate(b):
                if abs(val1 - val2) >= 2:
                    return True
        return False
    else:
        return False


if __name__ == "__main__":
    s = input()
    res = solve(s)
    if res:
        print("YES")
    else:
        print("NO")
