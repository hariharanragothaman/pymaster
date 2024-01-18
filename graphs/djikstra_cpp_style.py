#!/usr/bin/env python
from heapq import heappop, heappush


def dijkstra(graph, start=0):
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        _a, _b, _w = input().split()
        a, b, w = int(_a) - 1, int(_b) - 1, float(_w)
        graph[a].append((b, w))
        graph[b].append((a, w))

    _, parents = dijkstra(graph)
    if parents[n - 1] == -1:
        print(-1)
    else:
        res, parent = [], n - 1
        while parent != parents[0]:
            res.append(parent + 1)
            parent = parents[parent]
        res.reverse()
        print(*res)


if __name__ == "__main__":
    main()
