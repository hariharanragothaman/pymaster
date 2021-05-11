def maximum_subarray_sum(arr, n):
    left, right = 0, 0
    current_sum = 0

    # To account if this just contains one element
    max_sum = arr[left]

    # Basic Sliding window recipe

    for i in range(n):
        current_sum += arr[i]
        right = i
        max_sum = max(max_sum, current_sum)

        # Accounting for negative, and if current_sum < 0
        while left <= right and current_sum < 0:
            current_sum -= arr[left]
            left += 1

    return max_sum


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    maximum_sum = maximum_subarray_sum(arr, n)
    print(maximum_sum)