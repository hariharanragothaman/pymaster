#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : suffix_sum.py
# Author            : cppygod
# Date              : 08.11.2022
# Last Modified Date: 08.11.2022
# Last Modified By  : cppygod
"""
செயல் பேசும் ஆழம் இங்கே சொற்கள் பேசுமா?

Focus, Determination and Sheer-Will

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from functools import reduce


# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


def debug():
    if os.path.exists("data.in"):
        print("*" * 10)


def debug2(value):
    if os.path.exists("data.in"):
        print(value)


def debug3():
    if os.path.exists("data.in"):
        print("-" * 10)


def debug4(msg, value):
    if os.path.exists("data.in"):
        print(msg, value)


def debug5(msg):
    if os.path.exists("data.in"):
        print(msg)


start_time = time.time()


def solve(A, start, cnt, m, ans, n):
    if cnt >= m:
        return ans
    #  So basically we need to have more base conditions
    if cnt < m and start < 0:
        return ans
    else:
        ans += A[start]
        cnt += 1
        return solve(A, start - 1, cnt, m, ans, n)


def main():
    n, m = input_as_array()
    A = input_as_array()
    result = solve(A, start=n-1, cnt=0, m=m, ans=0, n=n)
    print(result)


if __name__ == "__main__":
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
