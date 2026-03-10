import heapq
from typing import *


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []

    array_iters = [iter(c) for c in sorted_arrays]

    for i, it in enumerate(array_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    print(min_heap)

    result = []

    """
    After adding the 1st elements of each list into the heap.
    Now, we need to get the next one right?
    Writing a for-loop to get those is memory / time intense.
    So that's where the iterator comes in...
    """
    while min_heap:
        small, small_idx = heapq.heappop(min_heap)
        # print(small, small_idx)
        result.append(small)
        array_iter_of_current_small_element = array_iters[small_idx]
        print(array_iter_of_current_small_element)

        next_element = next(array_iter_of_current_small_element, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, small_idx))

        # print("-" * 10)
    return result


A = [[3, 5, 7], [0, 6], [0, 6, 28]]
ans = merge_sorted_arrays(A)
print(ans)

print(list(heapq.merge(*A)))