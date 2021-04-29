from typing import List
from collections import defaultdict


def countComponents(n: int, g: List[List[int]]) -> int:
    visited = [False] * n
    count = 0

    for i in range(n):
        # Core Logic is: = If it's already visited - then it means it's already connected to something
        if visited[i]:
            continue
        else:
            count += 1

        stack = [i]
        while stack:
            node = stack.pop()
            for nei in g[node]:
                if not visited[nei]:
                    # If it's a neighbor, you can visit through this node
                    visited[nei] = True
                    stack.append(nei)

    return count


if __name__ == "__main__":
    vertices = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    result = countComponents(vertices, graph)
    print(result)
