#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : merge_sort.py
# Author            : cppygod
# Date              : 09.11.2022
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


def merge(A, start, pivot, end):
    n1 = pivot - start + 1
    n2 = end - pivot 

    L, R = [0] * n1, [0] * n2 

    # Populating both the arrays
    for i in range(0, n1):
        L[i] = A[start + i]

    for i in range(0, n2):
        R[i] = A[pivot+1+i]

    i = 0
    j = 0
    k = 1

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def solve(A, start, end):
    if start >= end:
        return 
    pivot = (start + end ) >> 1
    solve(A, start, pivot)
    solve(A, pivot+1, end)
    merge(A, start, pivot, end)

def main():
    n = int(input())
    A= input_as_array()
    solve(A, 0, n)

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
