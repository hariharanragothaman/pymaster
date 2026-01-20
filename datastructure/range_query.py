from math import log2

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


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    q = Query()
    min_value = q.RMQ(A, len(A), 3, 7)
    print("Basic RMQ::The min value is:", min_value)
