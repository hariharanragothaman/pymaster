"""
This is the Apple Division problem from CSES.
TL; DR - Split array into sets such that difference is minimal and print the difference
So ideally we are selecting elements for each subset --> here we are dividing it into 2 subsets.
"""

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


def debug3():
    if os.path.exists("data.in"):
        print("-" * 10)


def debug2(value):
    if os.path.exists("data.in"):
        print(value)


start_time = time.time()


def solve(A, n):
    total = sum(A)
    ans = float("inf")
    limit = 1 << n

    # Going through all the combinations generated
    for msk in range(limit):
        s = 0
        # Remember Length of the bit-array
        for j in range(0, n):
            # Check and get if the ith bit is set
            if msk & (1 << j):
                s += A[j]
            current_difference = abs((total - s) - s)
            ans = min(ans, current_difference)
    print(ans)


def main():
    n = int(input())
    A = input_as_array()
    solve(A, n)


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
