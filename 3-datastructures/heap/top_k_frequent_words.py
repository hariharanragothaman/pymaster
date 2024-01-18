from collections import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        # Counter based solution
        ctr = Counter(words)
        ctr = {k:v for k,v in sorted(ctr.items(), key=lambda x: (-x[1], x[0]))}
        return list(ctr.keys())[:k]     
        """

        counts = Counter(words)        
        heap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(heap)        
        return [heapq.heappop(heap)[1] for _ in range(k)]
