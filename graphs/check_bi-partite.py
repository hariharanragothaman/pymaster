# Check if graph is bi-partite -- Graph Theory
# Check if graph is a Tree?
"""
Recall that a graph is bipartite
if we can split it's set of nodes into two independent subsets A and B
such that every edge in the graph has one node in A and another node in B.
"""

from collections import defaultdict

def check_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    for start in range(range(n)):
        if color[start] == -1:
            color[start] = 0
            stack = [start, ]

            while stack:
                parent = stack.pop()
                for child in graph[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[child] == color[parent]:
                        return False, color
    return True, color

# constructing the graph
inp = [[1,3], [0,2], [1,3], [0,2]]
adj_map = defaultdict(list)
for u, v in enumerate(inp):
    adj_map[u].append(v)

result = check_bipartite(adj_map)
print("Is the graph bi-partite?: ", result)