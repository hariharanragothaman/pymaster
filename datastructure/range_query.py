import sys
from math import log2
sys.setrecursionlimit(100000)

class PrefixSum:
    @staticmethod
    def get_prefix_sum(self, A):
        n = len(A)
        PS = [0] * (n + 1)
        for i in range(1, n + 1):
            PS[i] = PS[i - 1] + A[i - 1]
        print("The prefix sum array is:", PS)
        return PS

    @staticmethod
    def get_sum(self, A, l, r):
        total = 0
        for i in range(l, r + 1):
            total += A[i]
        return total

class RangeQuery:
    """
    Range Query to get min and max b/w left and right
    """
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(
            self._data[depth][start], self._data[depth][stop - (1 << depth)]
        )

    def __getitem__(self, idx):
        return self._data[0][idx]

class Query:
    def __init__(self):
        MAX = 500
        self.lookup = [[0 for j in range(MAX)] for i in range(MAX)]

    def pre_process(self, arr, n):
        for i in range(n):
            self.lookup[i][i] = i

        for i in range(n):
            for j in range(i + 1, n):
                # This can be varied for max algorithm also
                if arr[self.lookup[i][j]] < arr[j]:
                    self.lookup[i][j] = self.lookup[i][j - 1]
                else:
                    self.lookup[i][j] = j

    def RMQ(self, arr, n, left, right):
        self.pre_process(arr, n)
        print(
            "Basic RMQ::The minimum b/w left and right is:",
            arr[self.lookup[left][right]],
        )
        return arr[self.lookup[left][right]]

class SparseTable:
    def __init__(self):
        MAX = 500
        self.lookup = [[0 for j in range(MAX)] for i in range(MAX)]

    def preprocess(self, arr: list, n: int):
        global lookup

        # Initialize M for the
        # intervals with length 1
        for i in range(n):
            lookup[i][0] = i

        # Compute values from
        # smaller to bigger intervals
        j = 1
        while (1 << j) <= n:

            # Compute minimum value for
            # all intervals with size 2^j
            i = 0
            while i + (1 << j) - 1 < n:

                # For arr[2][10], we compare
                # arr[lookup[0][3]] and
                # arr[lookup[3][3]]
                if arr[lookup[i][j - 1]] < arr[lookup[i + (1 << (j - 1))][j - 1]]:
                    lookup[i][j] = lookup[i][j - 1]
                else:
                    lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]

                i += 1
            j += 1

    # Returns minimum of arr[L..R]
    def query(self, arr: list, L: int, R: int) -> int:
        global lookup

        # For [2,10], j = 3
        j = int(log2(R - L + 1))

        # For [2,10], we compare
        # arr[lookup[0][3]] and
        # arr[lookup[3][3]],
        if arr[lookup[L][j]] <= arr[lookup[R - (1 << j) + 1][j]]:
            return arr[lookup[L][j]]
        else:
            return arr[lookup[R - (1 << j) + 1][j]]

    # Prints minimum of given
    # m query ranges in arr[0..n-1]

    def RMQ(self, arr: list, n: int, left, right):

        # Fills table lookup[n][Log n]
        self.preprocess(arr, n)
        print(self.query(arr, left, right))

"""
Some background as to why we need segment trees.

Consider these 2 problems
1. sum of elements from index 'low' to index 'high'
2. Change the value of a specified element in an array to a new value ~ say 'a'

Naive Solutions:

> run a loop from l to r and calculate the sum of elements in the range  - O(n)
> Updating a value takes - O(1)
-------------------------------------------------------------------

Another solution is:
> Copy the array
> Apply prefix sum - then sum can be found in O(1)
> Updating takes O(n) now.

How can we perform both operations in O(logn) time?
"""
class SegmentTree:
    def __init__(self, arr, function=min):
        # Making the length of the array the power of 2
        self.tree = [None for _ in range(len(arr))] + arr
        self.size = len(arr)
        self.fn = function
        self.build_tree()

    def build_tree(self):
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, p, v):
        p += self.size
        self.tree[p] = v
        while p > 1:
            p = p // 2
            self.tree[p] = self.fn(self.tree[p * 2], self.tree[p * 2 + 1])

    def query(self, l, r):
        l, r = l + self.size, r + self.size
        res = None
        while l <= r:
            if l % 2 == 1:
                res = self.tree[l] if res is None else self.fn(res, self.tree[l])
            if r % 2 == 0:
                res = self.tree[r] if res is None else self.fn(res, self.tree[r])
            l, r = (l + 1) >> 1, (r - 1) >> 1
        return res

class SegmentTreeFaster:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size : _size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Range Query Class
    arr = [5, 8, 6, 3, 2, 7, 2, 6]
    range_obj = RangeQuery(arr)
    op = range_obj.query(2, 5)
    print(op)

    # Segment Tree
    arr = [5, 8, 6, 3, 2, 7, 2, 10]
    seg_obj = SegmentTree(arr, function=max)
    print(seg_obj.tree)
    result = seg_obj.query(0, 7)
    result = seg_obj.query(2, 2)
    result = seg_obj.query(2, 5)
    print("The result is: ", result)


    # SegmentTreeFaster
    n, q = map(int, input().split())
    data = list(map(int, input().split()))
    # st = SegmentTree(data=data, func=lambda x, y: x + y)
    st = SegmentTreeFaster(data=data)
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        print(st.query(l, r + 1))
    item = st.__getitem__(4)
    print(item)

    q = Query()
    min_value = q.RMQ(A, len(A), 3, 7)
    print("Basic RMQ::The min value is:", min_value)
