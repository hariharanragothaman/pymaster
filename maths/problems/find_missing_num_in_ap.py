"""
Given an AP, find the missing number in AP
"""

def missing_number_ap(arr):
    # Sum of AP is - (first + last) * (n+1) / 2
    s = (arr[0] + arr[-1]) * (len(arr) + 1) // 2
    return s - sum(arr)

# A(n) = a + (n-1) * d - Using this formula binary search can also be applied
def missingNumber(self, A):
    n = len(A)
    d = (A[-1] - A[0]) / n
    left, right = 0, n

    while left < right:
        mid = (left + right) / 2
        if A[mid] == A[0] + d * mid:
            left = mid + 1
        else:
            right = mid
    return A[0] + d * left

if __name__ == '__main__':
    arr = [5, 7, 11, 13]
    op = missing_number_ap(arr)
    print(op)