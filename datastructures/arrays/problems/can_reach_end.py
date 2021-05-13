"""
Given an array A - if the ith index is denoting the maximum you can advance -
return whether one can reach the end of the array
"""


def can_reach_end(arr):
    start, end = 0, len(arr) - 1
    # basically take the greedy approach - but that might not always work
    # [2, 4, 1, 1, 0, 2, 3]
    # We can keep computing the max index to which it can jump
    i = 0
    # start point is always leading i & is less than 'end'
    while i <= start < end:
        start = max(start, i + arr[i])
        i += 1
    return start >= end


if __name__ == '__main__':
    arr = [3, 3, 1, 0, 2, 0, 1]
    arr2 = [3, 2, 0, 0, 2, 0, 1]
    can_reach_end(arr2)
