# DP Problem # 19

from typing import List


# Tested Solution in Leetcode:
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for n in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + n)
        print(f"The prefix sum is {self.prefix_sum}")

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]


def subarray_sums_brute_force(numbers: List[int], queries: [List[tuple]]) -> List[int]:
    return [sum(numbers[start:end+1]) for start, end in queries]


def subarray_sum_dp_prefix_sum(numbers: List[int], queries: [List[tuple]]) -> List[int]:
    """
    Args:
        numbers: List of numbers
        queries: queries are in the form a tuple (start, end)
    Returns:
    """
    prefix_sum = [numbers[0]]
    for i in range(len(numbers)):
        prefix_sum.append(prefix_sum[-1] + numbers[i])
    print(f"The prefix sum is: {prefix_sum}")
    return [prefix_sum[end+1] - prefix_sum[start] for start, end in queries]


if __name__ == '__main__':
    arr = [2, 5, 7, 1, 3, 8]
    queries = [(0, 2), (3, 5), (1, 4)]
    print(f"The numbers are: {arr}")
    print(f"Subarray sum through bruteforce: {subarray_sums_brute_force(arr, queries)}")
    print(f"Subarray sum through prefix-sum is: {subarray_sum_dp_prefix_sum(arr, queries)}")