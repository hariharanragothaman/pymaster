from typing import List


def reorder_even_odd(nums: List[int]) -> List[int]:
    # We want to do this with as little extra memory as possible
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] % 2 == 0:
            start += 1
        else:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
    print(f"The reordered array is: {nums}")


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    reorder_even_odd(arr)