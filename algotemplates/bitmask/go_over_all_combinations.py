def solve(A, n):
    total = sum(A)
    ans = float("inf")
    limit = 1 << n

    # Going through all the combinations generated
    for msk in range(limit):
        s = 0
        # Remember Length of the bit-array
        for j in range(0, n):
            # Check and get if the ith bit is set
            if msk & (1 << j):
                s += A[j]
            current_difference = abs((total - s) - s)
            ans = min(ans, current_difference)
    print(ans)
