from typing import *
from collections import *
from heapq import *


def minimumCost(self, n: int, A: List[List[int]]) -> int:
    G = defaultdict(list)
    for u, v, cost in A:
        G[u].append((v, cost))
        G[v].append((u, cost))
    print(G)

    # Using Djikstra
    PQ = [(0, 1)]
    heapify(PQ)
    visited = set()
    total = 0

    while PQ:
        cost, node = heappop(PQ)
        if node in visited:
            continue
        visited.add(node)
        total += cost
        for nei, nei_cost in G[node]:
            if nei not in visited:
                heappush(PQ, (nei_cost, nei))

    return total if len(visited) == n else -1