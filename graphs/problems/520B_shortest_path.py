import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

start_time = time.time()
"""
Vasya has found a strange device. On the front panel of a device there are: a red button, a blue button and a display showing some positive integer. 
After clicking the red button, device multiplies the displayed number by two. 
After clicking the blue button, device subtracts one from the number on the display. 
If at some point the number stops being positive, the device breaks down. The display can show arbitrarily large numbers. 
Initially, the display shows number n.
Bob wants to get number m on the display. What minimum number of clicks he has to make in order to achieve this result?
"""


def main():
    """
    Main function dedicated to get the I/P
    a, b = map(int, input().split())
    solve(a, b)
    """
    limit = 100000
    a, b = map(int, input().split())
    dist = [-1] * limit
    dist[a] = 0

    q = deque([])
    q.append(a)

    while q:
        node = q.popleft()
        nxt = node - 1
        if nxt >= 0 and dist[nxt] == -1:
            dist[nxt] = dist[node] + 1
            q.append(nxt)

        nxt = node * 2
        if nxt < limit and dist[nxt] == -1:
            dist[nxt] = dist[node] + 1
            q.append(nxt)

    print(dist[b])


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
