from typing import *

"""
Take in increasing groups and increasing sum
"""

def maximumGroups(self, A: List[int]) -> int:
    A = sorted(A)
    n = len(A)
    csum = 0
    total = 0
    cnt = 0
    ctake = 0
    take = 0

    for i in range(n):
        ctake += 1
        csum += A[i]

        if ctake > take and csum > total:
            take = ctake
            total = csum
            cnt += 1
            csum = 0
            ctake = 0

    return cnt
