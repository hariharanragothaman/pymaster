"""
NOTE: The heapq library only provides min-heap functionality
If you want max-heap - you need to write custom methods.
"""

import heapq

A = [1, 5, 3, 2, 4]

# Transform the List into heap in-place
heapq.heapify(A)
print(A)

# Get the n number of smaller and largest values
big_2 = heapq.nlargest(2, A)
print(big_2)

small_2 = heapq.nsmallest(2, A)
print(small_2)

# Pop the smallest element in the library
small = heapq.heappop(A)
print(A, small)

# Push a value into the heap and then pop and return the smallest element
small_after_update = heapq.heappushpop(A, 7)
print(small_after_update)

# Print the smallest element of the heap without popping it
e = A[0]
print(A, e)