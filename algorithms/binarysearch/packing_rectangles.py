# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 16:06:24
# @Last Modified by:   Hariharan Ragothaman
# @Last Modified time: 2022-04-09 18:19:11

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


start_time = time.time()


def main():
    width, height, n = input_as_array()
    """
    It is required to find the smallest square in which all the 
    rectangles can be packed.
    """


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
