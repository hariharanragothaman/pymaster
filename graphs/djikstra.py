# So this is a weighted graph - it can be directed or undirected

from heapq import heappop, heappush
from collections import defaultdict


def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    vertex = list(range(1, n+1))
    dist = [float("inf")] * n
    initial = [-1] * n

    distance_map = dict(zip(vertex, dist))
    parents_map = dict(zip(vertex, initial))

    distance_map[start] = 0
    queue = [(0, start)]

    while queue:
        path_length, vertex = heappop(queue)
        if path_length == distance_map[vertex]:
            for nei, edge_length in graph[vertex]:
                if edge_length + path_length < distance_map[nei]:
                    distance_map[nei] = edge_length + path_length
                    parents_map[nei] = vertex
                    heappush(queue, (edge_length + path_length, nei))
    return distance_map, parents_map


# Initial I/P
inp = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
start = 2

# Build the graph:
graph = defaultdict(list)

for v in inp:
    source, target, weight = v[0], v[1], v[2]
    graph[source].append((target, weight))
print("The initial graph is:", graph)  # Perfect understanding

dist_map, parents_map = dijkstra(n, graph, start)

print("The graph is", graph)
print("The final distance_map is:", dist_map)
print("The final parents map is:", parents_map)
