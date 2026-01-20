from typing import *


def canPartitionKSubsets(A: List[int], k: int) -> bool:
    """
    We are able to smell the related topic.
    Now, we need to figure out the implementation
    """
    total = sum(A)
    if total % k != 0:
        return False

    target = total // k
    n = len(A)
    visited = [False] * n

    def solve(subset_count, current_total):
        n = len(A)
        if subset_count == k - 1:
            return True

        if current_total > target:
            return False

        """
        When current subset sum reaches
        """
        if current_total == target:
            return solve(subset_count + 1, 0)

        for j in range(n):
            if not visited[j]:
                visited[j] = True

                if solve(subset_count, current_total + A[j]):
                    return True

                # Backtrack the step we took
                visited[j] = False

        # no combination was found..
        return False

    return solve(0, 0)


def can_partition_k_subsets_optimized(A, k):
    total = sum(A)
    if total % k != 0:
        return False

    n = len(A)
    target = total // k
    visited = [False] * n

    A = sorted(A, reverse=True)

    def solve(index, count, current_total):
        if count == k - 1:
            return True
        if current_total > target:
            return False
        if current_total == target:
            return solve(0, count + 1, 0)

        for j in range(index, n):
            if not visited[j]:
                visited[j] = True
                if solve(j + 1, count, current_total + A[j]):
                    return True

                # Now we need to back-track
                visited[j] = False

        return False

    return solve(0, 0, 0)
