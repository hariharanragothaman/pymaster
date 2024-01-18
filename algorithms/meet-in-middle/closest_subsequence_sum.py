from typing import List
from bisect import bisect_left

"""
Sharing some of my fundamental learnings / observations.

When the constraints are low, for example - length of the array is <=40, my initial thought process was to brute-force.
When brute-force doesn't work, and ends up giving us TLE, then - we can think about "Meet in the Middle" approach
Before going into the "Meet-in-the-Middle" approach, let's first try to understand some subproblems clearly, even when we bruteforce.

Thoughts leading to the solution:

First, I need to select the elements, that I need to part of the subsequence.
For which I need to figure out the various combinations of elements to pick and choose.
One of the techniques, I use to pick combination of elements, as part of a subsquence is to use "BitMask"

Consider the following function below:
"""
"""
class Solution:
    def get_subset_sums(self, A: List[int]):
        result = set()
        n = len(A)
        limit = 1 << n
        # Going through all the combinations generated
        for msk in range(limit):
            s = 0
            # Going through the length of the array
            for j in range(0, n):
                # Check if the i'th bit is set, to choose the element from the array
                if msk & (1 << j):
                    s += A[j]
            result.add(s)
        return result
"""

"""
In the above function, I have added comments for clarity, but we are really doing in simple terms is:

Let's say the array consists of 3 elements; A = [1, 2, 3]
The total number of combinations is 2^3 = 8
This can be represented in binary.
0 - 000
1 - 001
2 - 010
3 - 011
4 - 100
5 - 101
6 - 110
7 - 111
Here in the above binary representations, each binary number is telling us what number to pick from the array, thus giving us all possible subsequences.
Hence in the function get_subset_sums we merely check if the i'th bit is set, and if it is, include it when computing the sum of the subsequence.
Hence, for a given input array - the function gives us all possible subsequence sums.
Okay? - Now can we go over all the various sub-sequences, and see which is closest to goal? We can, but this will result in TLE
Now to optimize, this - here, we think about the "Meet in the Middle" approach.
Meet in the Middle Approach:

Here, we decide to split the I/P array into 2 parts. Let's say A1 and A2
Now, let's get the subsequence sums for A1, and A2 calling the get_subset_sums function above.
Let x be the sum we select from s1
Let y be the sum we select from s2
So x + y = sum - where-in the sum should be as close to the goal as possible.
Taking some smart approaches.

Hence for every value 'y' in s2, we search for a value 'x' in s1 such that x + y is almost goal
This search can be implemented using binary search.
Hence the entire solution looks as follows:
"""


class Solution:
    def get_subset_sums(self, A: List[int]):
        result = set()
        n = len(A)
        limit = 1 << n
        # Going through all the combinations generated
        for msk in range(limit):
            s = 0
            # Going through the length of the array
            for j in range(0, n):
                # Check if the i'th bit is set, to choose the element from the array
                if msk & (1 << j):
                    s += A[j]
            result.add(s)
        return result

    def minAbsDifference(self, A: List[int], goal: int) -> int:
        n = len(A)
        half = n >> 1
        A1, A2 = A[:half], A[half:]
        s1, s2 = self.get_subset_sums(A1), self.get_subset_sums(A2)
        s2 = sorted(s2)

        # Note: s1, s2 are representations of what elements we are selecting from A1, A2
        # let x be the sum we select from s1
        # let y be the sum we select from s2
        # So x + y = sum should be as close to the goal as possible
        #   x (s1) + y (s2) == sum
        # so that - abs(sum - goal) is as minimum as possible

        # Hence for every value 'y' in s2, we search for a value 'x' in s1
        # such that x + y is almost goal  - only then sum-goal is as small as possible.
        # So we search "goal-y" in s1

        ans = float("inf")

        for s in s1:
            remain = goal - s
            # binary search for the value in s2 that's closest to the remaining value
            i2 = bisect_left(s2, remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(remain - s2[i2 - 1]))
        return ans


"""
Submission Link: https://leetcode.com/submissions/detail/768998569/

After thoughts:

Looking at other solutions in the discuss section, the get_subset_sums function can be written much faster and nicer.
For example:

def fn(nums):
    ans = {0}
    for x in nums:
        ans |= {x + y for y in ans}
    return ans
Also the OJ limits are a bit tight for this question, when I submitted my same solution that got AC, sometimes I get TLE, sometimes I get AC
Nevertheless, I thought sharing my whole thought process here might be useful.
"""
