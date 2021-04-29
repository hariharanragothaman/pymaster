# Most generalized binary search
"""
Suppose we have a search space. It could be an array, a range, etc.
Usually it's sorted in ascend order.
For most tasks, we can transform the requirement into the following generalized form:
"""

from typing import List

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

"""
We need to modify only 3 parts in the above template for any binary-search

1. Correctly initialize the boundary variables, left, right - include all possible elements
2. Decide return value
   Is it left (or) left - 1? - So it can be left or left -1
   Remember this: After exiting the loop, left is the minimal k satisfying the condition function
3. Design the condition function
"""

###################### Let's apply the templates to the following problems


# Problem-1
"""
You are a product manager and currently leading a team to develop a new product. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad. 
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. 
You are given an API bool isBadVersion(version) which will return whether version is bad.
"""

def isBadVersion(pivot):
    """ Internal API"""
    pass

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 0, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


# Problem-2

"""
Implement int sqrt(int x). Compute and return the square root of x, where x is guaranteed to be a non-negative integer. 
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""
def mySqrt(x):
    left, right = 0, x
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid
    return left - 1

"""
There's one thing I'd like to point out. 
Remember I say that we usually look for the minimal k value satisfying certain condition? 
But in this problem we are searching for maximal k value instead.
Feeling confused? Don't be. 
Actually, the maximal k satisfying condition(k) is False is 
just equal to the minimal k satisfying condition(k) is True minus one. 
This is why I mentioned earlier that we need to decide which value to return, left or left - 1.
"""

# Problem3 - Search Insert Position

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
"""
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left ) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left