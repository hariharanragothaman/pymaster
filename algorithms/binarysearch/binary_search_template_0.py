from bisect import bisect_left

"""
Sharing this code-snippet:
Sometimes, when we are searching we might not know if it's idx, idx-1

for s in sums1:
    remain=goal-s
    # binary search for the value in s2 that's closest to the remaining value
    i2 = bisect_left(s2,remain)
                    
    if i2 < len(s2):
        ans = min(ans,abs(remain-s2[i2]))
    if i2 > 0:
        ans = min(ans,abs(remain-s2[i2-1]))
        
return ans
"""


# TEMPLATE #1: Usual approach - when we know the number exists, and we are searching for it's index
def binary_search_gen(array, target):
    if len(array) == 0:
        return -1

    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Smarter Template for getting the middle value
def binary_search_smart():
    left, right = 0, 10 ** 18
    condition = None
    while left < right:
        mid = left + right + 1 >> 1
        if condition:
            left = mid
        else:
            right = mid - 1


# TEMPLATE #2 - Advanced Binary Search
def binary_search_advanced(array, target):
    if len(array) == 0:
        return -1
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) >> 1
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left != len(array) and array[left] == target:
        return left
    return -1


# TEMPLATE #3 - Advanced Binary Search II
def binary_search_new(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


# TEMPLATE #4 - Bisect and its advantages
# Binary search recipe using bisect
def binary_search(array, val):
    index = bisect_left(array, val)
    if index != len(array) and array[index] == val:
        return index
    else:
        return -1


if __name__ == "__main__":
    arr = [2, 4, 5, 8, 10]
    value = 4
    res = binary_search(arr, 1)
    print(res)
