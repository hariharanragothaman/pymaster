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
            l, r = (l + 1) // 2, (r - 1) // 2
        return res


if __name__ == "__main__":
    arr = [5, 8, 6, 3, 2, 7, 2, 10]
    seg_obj = SegmentTree(arr, function=lambda x, y: x + y)
    print(seg_obj.tree)
    result = seg_obj.query(2, 2)
    print("The result is: ", result)
