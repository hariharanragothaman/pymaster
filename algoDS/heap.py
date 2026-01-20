import heapq
from typing import List, Iterable, TypeVar
from collections import Counter

T = TypeVar("T")


class Heap:
    """Thin wrapper around Python's heapq (min-heap)."""
    @staticmethod
    def make_heap(items: List[T]) -> List[T]:
        heapq.heapify(items)
        return items

    @staticmethod
    def get_n_largest(items: Iterable[T], n: int) -> List[T]:
        return heapq.nlargest(n, items)

    @staticmethod
    def get_n_smallest(items: Iterable[T], n: int) -> List[T]:
        return heapq.nsmallest(n, items)

    @staticmethod
    def pop_smallest(heap: List[T]) -> T:
        """Pop and return the smallest element from the heap."""
        return heapq.heappop(heap)

    @staticmethod
    def push_value_and_pop(heap: List[T], value: T) -> T:
        """Push a value, then pop and return the smallest element."""
        return heapq.heappushpop(heap, value)

    @staticmethod
    def top_K_frequent(words: List[T], k: int) -> List[T]:
        H = Counter(words)
        heap = [((-count, word) for word, count in H.items())]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
