#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : find_subsequence_of_K_largest_sum.py
# Author            : cppygod
# Date              : 22.01.2022
# Last Modified Date: 22.01.2022
# Last Modified By  : cppygod


import heapq
from collections import Counter


def subsequence_of_length_k_max_sum(nums, k):
    """
    Push elements into a heap
    if heap length is > k then keep popping.
    heapq - will return the smallest element only, and keep the larger elements
    """

    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    print("The heap is:", heap)

    cnt = Counter(heap)
    res = []

    # This is done to preserve the order of the subsequence and get the values from the heap
    for n in nums:
        if cnt[n] > 0:
            cnt[n] -= 1
            res.append(n)

    return res
