"""
Given an integer in the form of an array, increment it.
"""


def plus_one(nums):
    """Implement grade school algorithm to increment numbers"""
    print(f"The I/P array is: {nums}")
    nums[-1] += 1
    n = len(nums)

    # Go until the first element
    for i in range(n - 1, 1, -1):
        if nums[i] != 10:
            break
        else:
            nums[i] = 0
            nums[i - 1] += 1

    if nums[0] == 10:
        nums[0] = 1
        nums.append(0)

    print(*nums)


if __name__ == "__main__":
    nums = [1, 2, 9]
    plus_one(nums)
