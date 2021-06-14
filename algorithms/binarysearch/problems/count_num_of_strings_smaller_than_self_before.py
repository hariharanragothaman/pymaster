
# Problem Statement https://www.hackerearth.com/practice/codemonk/

from collections import defaultdict
from bisect import bisect_left


def solve(A):
    s_arr = sorted(A)
    hmap = defaultdict(int)
    cnt = 0
    for c in s_arr:
        hmap[c] = cnt
        cnt += 1

    result = []
    visited = []

    for i, c in enumerate(A):
        idx = bisect_left(visited, c)
        visited.insert(idx, c)
        result.append(idx)

    for c in result:
        print(c)


if __name__ == '__main__':
    n = int(input())
    i = 0
    arr = []
    while i < n:
        s = input()
        arr.append(s)
        i += 1
    solve(arr)