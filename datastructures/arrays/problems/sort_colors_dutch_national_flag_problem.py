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
    """ The sort Colors() problem is just a variant of the dutch national flag problem, where the pivot is 1 """
    dutch_flag_partition(nums, pivot=1)


def dutch_flag_partition(nums, pivot):
    """ Idea is to group the elements in-place"""
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


if __name__ == '__main__':
    pass
