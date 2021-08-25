def get_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    print("The prefix sum array is:", prefix_sum)
    return prefix_sum
