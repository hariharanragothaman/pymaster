# Check if graph is bi-partite -- Graph Theory

"""
Recall that a graph is bipartite
if we can split it's set of nodes into two independent subsets A and B
such that every edge in the graph has one node in A and another node in B.

It turns out the graph is bipartite, when it does not contain a cycle, with
an odd number of edges.

"""
from collections import defaultdict
from typing import List


def check_bipartite(graph: List[List[int]]) -> bool:
    adj_map = defaultdict(list)
    for i, c in enumerate(graph):
        adj_map[i] = c
    print(adj_map)

    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            stack = [start]

            while stack:
                parent = stack.pop()

                for child in adj_map[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[parent] == color[child]:
                        return False
    return True


if __name__ == "__main__":
    # constructing the graph
    inp = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    result = check_bipartite(inp)
    print("Is the graph bi-partite?: ", result)
