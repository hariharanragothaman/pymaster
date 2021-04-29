from collections import defaultdict


def topo_sort_variant(graph, n):
    # Returns a topologically sorted graph
    res = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack[-1]
                if not visited[node]:
                    visited[node] = True
                    for child in graph[node]:
                        if not visited[child]:
                            stack.append(child)
                else:
                    result.append(stack.pop())
    return res


if __name__ == "__main__":
    min_roads_required = 0
    # Cities are vertexes and roads are the edges
    ncities, nroads = map(int, input().split())
    g = defaultdict(list)
    for i in range(nroads):
        u, v = map(int, input().split())
        g[u].append(v)

    result = topo_sort_variant(g, ncities)
