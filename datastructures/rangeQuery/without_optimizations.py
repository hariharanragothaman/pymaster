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
