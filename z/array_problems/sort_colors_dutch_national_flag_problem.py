"""
The question is to group all same integers together - Sort colors in place
The challenge is: - They can give a pivot index
                    They can also to do this in-place

Generic version of the problem:
- Given an I/P array - rearrange the elements such that all elements less than pivot appear first,
                    - followed by element equal to the pivot
                    - followed by elements greater than the pivot
"""


def sortColors(nums):
    """The sort Colors() problem is just a variant of the dutch national flag problem, where the pivot is 1"""
    dutch_flag_partition(nums, pivot=1)


def dutch_flag_partition(nums, pivot):
    """Idea is to group the elements in-place"""
    n = len(nums)

    left = 0

    # Group elements smaller than pivot
    for i in range(n):
        if nums[i] < pivot:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1

    # Second pass group elements larger than the pivot
    right = n - 1
    for i in reversed(range(n)):
        if nums[i] > pivot:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1


def dutch_flag_partition_optimized(nums, pivot):
    """
    here the idea is:
        1. If value is less than pivot - we exhange it with the first pivot occurrence
        2. If value is equal to the pivot - we advance to the next unclassified element
        3. If the value is greater then the pivot = - we exchange it with the last unclassified element
    """
    smaller = 0
    equal = 0
    larger = len(nums) - 1

    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller += 1
            equal += 1
        elif nums[equal] == pivot:
            equal += 1
        elif nums[equal] > pivot:
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1


if __name__ == "__main__":
    pass
