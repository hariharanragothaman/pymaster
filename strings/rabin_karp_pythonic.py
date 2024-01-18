"""
To find the first occurrence of substring ~ using Robin Karp
Solution Approach:

"""
from functools import reduce


def rabin_karp(t, s):
    if len(s) > len(t):
        return -1

    base = 26

    # Base hash codes computing for 's' and 't'
    t_hash = reduce(lambda h, c: h * base + ord(c), t[: len(s)], 0)
    s_hash = reduce(lambda h, c: h * base + ord(c), s, 0)

    print("The thash is:", t_hash)
    print("The shash is:", s_hash)

    power_s = base ** max(len(s) - 1, 0)  # base ^ |s-1|
    print("The power_s is:", power_s)

    for i in range(len(s), len(t)):
        # Check for hashcode and actual string to avoid collision
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)

        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    return -1


if __name__ == "__main__":
    text = "GACGCCA"
    pattern = "CGC"
    result = rabin_karp(text, pattern)
    print(result)
