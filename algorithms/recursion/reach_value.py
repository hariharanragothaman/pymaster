#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : reach_value.py
# Author            : cppygod
# Date              : 08.11.2022
# Last Modified Date: 09.11.2022
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

"""
This is always increasing...

"""

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def solve(self, start, n):
        if start == n:
            self.count += 1
        elif start > n:
            return 
        else:
            self.solve(start * 10, n)
            self.solve(start * 20, n)

def main():
    n = int(input())
    s = Solution()
    s.solve(1, n)
    if s.count >= 1:
        print("YES")
    else:
        print("NO")
    debug()

if __name__ == "__main__":
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
