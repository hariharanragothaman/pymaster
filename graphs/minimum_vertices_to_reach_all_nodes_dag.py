"""
Given a directed acyclic graph, find the minimum number of vertices needed to reach all nodes
"""

from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        print(f"The graph is: {graph}")

        # Method 2 to solve
        values = graph.values()
        s = set([item for sublist in values for item in sublist])
        return [c for c in range(n) if c not in s]


if __name__ == "__main__":
    s = Solution()
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    op = s.findSmallestSetOfVertices(n, edges)
    print(f"The minimum set of vertices are {op}")
