def get_prefix_sum(A):
    n = len(A)
    PS = [0] * (n + 1)
    for i in range(1, n + 1):
        PS[i] = PS[i - 1] + A[i - 1]
    print("The prefix sum array is:", PS)
    return PS
