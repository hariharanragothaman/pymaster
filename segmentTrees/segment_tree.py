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
