"""
Given two strings text and pattern,
return the list of  start indexes in text that matches with the pattern
using knuth_morris_pratt algorithm.
If idx is in the list, text[idx : idx + M] matches with pattern.
Time complexity : O(N+M)
N and M is the length of text and pattern, respectively.
"""

def knuth_morris_pratt(text, pattern):
    n, m = len(text), len(pattern)
    pi = [0 for i in range(m)]
    i, j = 0, 0

    # making pi table
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret

def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi


def match(s, pat):
    pi = partial(pat)

    g, idx = 0, []
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            idx.append(i + 1 - g)
            g = pi[g - 1]

    return idx


def string_find(s, pat):
    pi = partial(pat)

    g = 0
    for i in range(len(s)):
        while g and pat[g] != s[i]:
            g = pi[g - 1]
        g += pat[g] == s[i]
        if g == len(pi):
            return True

    return False


if __name__ == "__main__":
    s = "HELLOWORLLD"
    p = "LL"
    res = string_find(s, p)
    print(res)

    text = "GACGCCACGC"
    pattern = "CGC"
    result = knuth_morris_pratt(text, pattern)
    print(f"The result is: {result}")
