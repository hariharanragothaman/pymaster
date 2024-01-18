"""
The whole idea of rangeQueries is to get min(l, r) | max(l, r) | sum(l, r)
"""

arr = [1, 3, 8, 4, 6, 1, 3, 4]


def get_sum(arr, l, r):
    total = 0
    for i in range(l, r + 1):
        total += arr[i]
    return total


# Naive way of getting the sum

result = get_sum(arr, 3, 6)
print("Full parsing::The sum between 3 and 6 is:", result)

"""
This function works in O(n) time - where n is the size of the array
So - for 'q' queries - it will take O(n*q) times 
"""

# Case-1 - Static array queries:
"""
Scenario: 
1. Array values are static
2. They are never updated between the queries
If the above 2 conditions are satisified - building a static data structure is enough

Enter the method - Prefix sum
"""

array = [1, 3, 4, 8, 6, 1, 4, 2]

print("Prefix Sum:: The initial array is:", array)
prefix_sum = [array[0]]

for i in range(1, len(array)):
    prefix_sum.append(prefix_sum[-1] + array[i])
print("Prefix Sum:: The prefix sum array is:", prefix_sum)

# For the sum between - say sum(3, 6)
left = 3
right = 6
print(
    "Sum between indexes 3 and 6 (0-indexed)", prefix_sum[right] - prefix_sum[left - 1]
)
# So here the sum can be calculated in O(1) time


"""
- So now let's look at how to find minimum queries
 Incoming - Sparse Table method
Note - Sparse tables can be used only - immutable arrays - arrays should not be modified
       array cannot be modified
"""

# Intuition for sparse table is that - any number can be represented as decreasing powers of two
# 13 - (1101) ( 8+4+1)
# With the same intuition - any interval can be represented as union of intervals with lengths that are
# decreasing powers of two

# [2,14]  = [2,9] union [10,13] union [14, 14]
"""
Just covering some pre-requisites
Method 1 - 2D array
Method 2 - Sqrt Decomposition
Method 3 - Sparse Table

O(n**2) - space and pre-processing
Here a lot of time is wasted in pre-processing
But the RMQ operation takes O(1) time
"""

nums = [1, 3, 4, 8, 6, 1, 4, 2]


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


q = Query()
min_value = q.RMQ(nums, len(nums), 3, 7)
print("Basic RMQ::The min value is:", min_value)


##### Sparse Table Lookup
# Python3 program to do range minimum query
# in O(1) time with O(n Log n) extra space
# and O(n Log n) preprocessing time
from math import log2


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
