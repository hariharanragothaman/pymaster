# region imports
import os, sys, math, cmath, time, collections
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi, log10
from collections import deque, Counter, OrderedDict, defaultdict
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from itertools import accumulate, permutations, combinations, combinations_with_replacement
from io import BytesIO, IOBase
from functools import reduce

# endregion

# region solution

def solve() -> None:
    pass

# endregion

# region testcase
def main() -> None:
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    start_time = time.time()
    testcases = 1

    for i in range(testcases):
        solve()
        debug('-')

    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()

# endregion

# region debug
def input_as_array() -> list[int]:
    return list(map(int, input().split()))

def debug(char) -> None:
    if os.path.exists("data.in"):
        print(char * 25)

def debug2(value) -> None:
    if os.path.exists("data.in"):
        print(value)

# endregion

# region fastio

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
