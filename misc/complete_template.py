import os
import sys
from io import BytesIO, IOBase

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

BUFSIZE = 8192

from collections import deque, Counter, OrderedDict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
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


if "PyPy" in sys.version:
    from _continuation import continulet
else:
    import threading


def binNumber(n, size=4):
    return bin(n)[2:].zfill(size)


def iar():
    return list(map(int, input().split()))


def ini():
    return int(input())


def isp():
    return map(int, input().split())


def sti():
    return str(input())


def par(a):
    print(" ".join(list(map(str, a))))


def tdl(outerListSize, innerListSize, defaultValue=0):
    return [[defaultValue] * innerListSize for i in range(outerListSize)]


def sts(s):
    s = list(s)
    s.sort()
    return "".join(s)


def bis(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return [i, True]
    else:
        return [-1, False]


class pair:
    def __init__(self, f, s):
        self.fi = f
        self.se = s

    def __lt__(self, other):
        return (self.fi, self.se) < (other.fi, other.se)


# ACTUAL CODE after getting Input is here
def main():
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    values = input().split()
    print(*values)


if __name__ == "__main__":
    if "PyPy" in sys.version:

        def bootstrap(cont):
            call, arg = cont.switch()
            while True:
                call, arg = cont.switch(
                    to=continulet(lambda _, f, args: f(*args), call, arg)
                )

        cont = continulet(bootstrap)
        cont.switch()

        main()

    else:
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
