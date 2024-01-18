"""
Given an integer array nums and an integer k, return the number of subarrays of nums 
where the greatest common divisor of the subarray's elements is k.

Hint: The number of distinct GCDs would not exceed log(m), where m is the maximum value in the array.

"""

from math import gcd
from collections import *


def subarrayGCD(self, nums: List[int], k: int) -> int:
    cnt = 0
    n = len(nums)
    hmap = Counter()

    for i in range(n):
        hmap1 = Counter()
        if nums[i] % k == 0:
            hmap[nums[i]] += 1

        for key, value in hmap.items():
            hmap1[gcd(key, nums[i])] += value

        cnt += hmap1[k]
        hmap, hmap1 = hmap1, hmap

    return cnt
  
def subarrayGCD2(self, nums: List[int], k: int) -> int:  
  n, cnt = len(nums), 0     
  for i in range(n):
      for j in range(i, n):
          if nums[j] % k == 0:
              nums[i] = gcd(nums[i], nums[j])
              cnt += (nums[i]== k)
          else:
              # Break, since we are checking sub-array
              break
          # print(nums)
  return cnt 
