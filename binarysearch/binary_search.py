
# TEMPLATE #1: Usual approach
def binary_search_gen(array, target):
    if len(array) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# TEMPLATE #2 - Advanced Binary Search

def binary_search_advanced(array, target):
    if len(array) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left+right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left != len(array) and nums[left] == target:
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
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1


# TEMPLATE #4 - Bisect and its advantages

from bisect import bisect_left
def binary_search(array, val):
    index = bisect_left(array, val)
    if index != len(array) and array[index] == val:
        return index
    else:
        return -1


if __name__ == '__main__':
    arr = [1, 2, 4, 4, 5, 6, 7]
    value = 4
    res = binary_search(arr, 7)
    print(res)