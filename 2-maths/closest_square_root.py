"""
Write a program which takes a non-negative integer and return the largest integer whose square
is less than or equal to the given integer.
16 - 4
300 - 17  { 17^2 - 289 and 289 < 300}
"""

# Linear approach is bruteforce, will take more than 10^9 iterations for 32 bit integer.


def compute_square_root(k):
    # Obviously we have to use binary search
    left, right = 0, k
    while left <= right:
        pivot = (left + right) // 2
        if pow(pivot, 2) <= k:
            left = pivot + 1
        else:
            right = pivot - 1
    return left - 1


op = compute_square_root(300)
print(op)
