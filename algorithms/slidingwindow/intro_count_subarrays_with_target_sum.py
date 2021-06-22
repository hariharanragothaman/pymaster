"""
To count the number of subarrays having a definite sum

Constraints:
The numbers are all +ve - 1 to 2*10^5

"""


""" 
For problems of this  sort, we need to use sliding window
"""


def count_subarrays_with_target_sum(arr, n, target):
    left = right = window_sum = result_count = 0

    while right < n:
        # Expanding the array
        window_sum += arr[right]
        if window_sum == target:
            result_count += 1

        # Contracting the array - if sum becomes greater
        while window_sum > target and left < right:
            # print("The window sum now is:", window_sum)
            window_sum -= arr[left]
            left += 1
            if window_sum == target:
                result_count += 1

        right += 1

    print(result_count)


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    count_subarrays_with_target_sum(arr, n, target)
