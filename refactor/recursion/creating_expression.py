#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : creating_expression.py
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


"""
The question is asking if we can put either '+' or '-'
between these numbers to get the value X 
Let's assume there are 3 numbers
1 2 3
n numbers -> n-1 operands
So here + and -
2 operands - 2^n combinations 
One way is to recursively go through all the combinations...

So what's the best recurse condition here?
Hmm. Thinking
Also in the question he is asking - YES or NO only.
So we can do + and - and then keep adding to a set()
if it's in visited then 'YES', else 'NO'
BFS can also be done in recursion? Right? Lol.
Okay good thinking.

In our recursive calls.. either + is going pr - is going
we need both

1 2 3 

1 + 2 = 3 
1 - 2 = -1

3 + 3
3 - 3

-1 + 3
-1 - 3

1 + 2 + 3
1 + 2

In implementation wise instead of popping, we can 
simply use indices 

Because in BFS you end up appending to the Queue
Here you can't append stuff? after you pop 
So use indices to your advantage...OK now, let's keep trying..

"""

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def solve(self, A, n, i, x, ans):
        if i == n:
            if ans == x:
                self.count += 1
        else:
            self.solve(A, n, i + 1, x, ans + A[i])
            self.solve(A, n, i + 1, x, ans - A[i])

def main():
    n, x = input_as_array()
    A = input_as_array()
    s = Solution()
    s.solve(A, n, 1, x, ans=A[0])
    if s.count > 0:
        print("YES")
    else:
        print("NO")


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
