"""
Fenwick Tree and it's applications

Let f(x) be some reversible function and A be an array of integers of length N

Fenwick tree is a datastructure that has the following properties
    a. Calculates the value of the function f in the given range [l,r] - in O(logn) time.
    b. updates the value of an element of A in O(logn) time.
    c. requires O(N) memory, exactly requires the same memory as of A
    d. is easy to use and code in 2D arrays

Fenwwick tree is also called as - Binary Indexed Tree or BIT
Note - Here f(x) can be any function - for quick understanding we can have it as a sum() function
"""

"""
Background:


1. Creating the Tree
2. Update the tree
3. Applying a function for the operation?


Concept# 1: 

Steps 1-3 - How to optimize?

Array has 11 elements
0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10

               [] (0)
0 - 0000
1 - 0001
2 - 0010
3 - 0011

Flip the right most bit (1)   
0 - 0000
1 - 0001 -> 0000 (0)
2 - 0010 -> 0000 (0)
3 - 0011 -> 0010 (2)
4 - 0100 -> 0000 (0)
.......
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

Tree? - number of elements in the array?

               [] (0)
    /       /      \    \
[](1)  [](2)   [](4)    [](8)
         /      / \         |   \    
     [](3)   [](5) [](6)   [](9)  [](10)
                    \               \
                    [](7)           [](11)

How to efficiently flip the right most bit? (optimization)
   
   
Concept #2:
Every number can be represented as sum of powers of 2
[](0) --> empty
1  = 0 + 2^0            ------> Starting from index 0 - sum of 1 element
2  = 0 + 2^1            ------> Starting from index 0 - sum of 2 elements
3  = 2^1 + 2^0          -----> Starting from index 2 - sum of 1 element
4  = 0 + 2^2           -------> Starting from index 0 - sum of 4 elements
5  = 2^2 +2^0          -------> Starting from index 4 - sum of 1 element
6  = 2^2 + 2^1
7  = 2^2 + 2^1 + 2^0  ---> Starting from index 6 sum of 1 element
8  = 0 + 2^3 ------> Starting from index 0 sum of 8 elements
9 =  2^3 + 2^0
10 =  2^3 + 2^1
11 = 2^3 + 2^1 + 2^0 ---> Starting frrom index 10 1 element

               [0] (0)
    /       /      \    \
[3](1)  [5](2)   [10](4)    [19](8)
(0,0)   (0,1)        (0,3)       (0,7)
         /      / \         |   \    
     [-1](3)   [5](5) [9](6)   [7](9)  [9](10)
     
                    \               \
                    [-3](7)           [3](11)

BIT = [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9, 11] - generate the BIT array


(0, 5) - subarray sum -->

 You have finished generating the BIT array
 (0,5) -- arr[6] 
 find parent of 6? arr[4]
 find parent of arr[4] -- arr[0]
 
 sum = arr[6] + arr[4] + arr[0] 
 
 
 (5, 10)
 f(0,11) - f(0, 5)
 
"""


"""
Actual template:

Getting the parent:
index = n 
1. Take 2's complement
2. AND with original number
3. SUBTRACT from original number

All 3 steps will be written in 1 line -> O(1)  complexity

"""
"""
BIT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Getting the next:
index = n 
1. Take 2's complement
2. AND with original number
3. ADD to original number
"""

# Time Complexity is
# Updates / calculating O(log(n)) time
# O(n) - memory


"""
It is obvious that there is no easy way of finding minimum of range [l,r] using Fenwick tree, 
as Fenwick tree can only answer queries of type [0,r]. 
Additionally, each time a value is update'd, the new value has to be smaller than the current value 
(because the min function is not reversible). These, of course, are significant limitations.

"""
from typing import List


class Fenwick:
    """Fenwick Tree Supports only Sum queries"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.BIT = [0] * (len(self.nums) + 1)
        for i in range(len(self.nums)):
            self.update(i, nums[i], True)
        print(self.BIT)

    def update(self, i: int, val: int, init=False) -> None:
        if not init:
            # only update the difference
            val, self.nums[i] = val - self.nums[i], val

        i += 1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & -i

    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.BIT[i]
            i -= i & -i
        return ans

    def sumRange(self, i: int, j: int) -> int:
        return self.query(j) - self.query(i - 1)


if __name__ == "__main__":
    nums = [6, 4, 1, 7, 3, 4, 2]
    f = Fenwick(nums)
    sum_between = f.sumRange(2, 5)
    print("The sum between the indexes is:", sum_between)
