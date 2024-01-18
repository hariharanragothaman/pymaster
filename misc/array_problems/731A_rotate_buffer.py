"""
Given a rotating buffer b/w a-z; we need to be forming a word
"""

import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right


start_time = time.time()


def solve(string):
    """
    Actual solution
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = [c for c in alpha]
    limit = list(range(0, 26))
    hmap = dict(zip(alpha, limit))

    cnt = 0

    start = "a"

    for ch in string:
        candidates = [hmap[start], hmap[start] + 26, hmap[ch], hmap[ch] + 26]
        print(candidates)
        candidates = sorted(candidates)

        total = float("inf")
        for c in zip(candidates, candidates[1:]):
            res = abs(c[0] - c[1])
            if res < total:
                total = res

        start = ch
        cnt += total

    print(cnt)


def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    s = input()
    solve(s)


if __name__ == "__main__":
    LOCAL = False

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("../io/data.in", "r")
        sys.stdout = open("../io/data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
