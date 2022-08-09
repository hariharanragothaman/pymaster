from collections import defaultdict


def split_array_with_same_avg(A):
    total = sum(A)
    n = len(A)

    for i in range(n):
        A[i] = n * A[i] - total

    # When an array is split into 2 arrays with same avg, the avg is the same as the avg of the whole array
    # We are looking for a non-empty strict subset of A that sums to zero
    X = set()
    for a in A[:-1]:  # excluding last element so it looks for STRICT subset
        X |= {a} | {a + x for x in X if x < 0}
        if 0 in X:
            return True
    return False
