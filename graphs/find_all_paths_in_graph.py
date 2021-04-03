
from collections import defaultdict


def find_all_paths(start, end, path=[]):
    """
    Given a graph, find all the paths - given start and destination
    """
    all_paths = []
    path = path + [start]

    if start == end:
        return [path]

    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(node, end, path)
            for np in new_paths:
                all_paths.append(np)
    return all_paths


if __name__ == '__main__':
    edges = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    graph = defaultdict(list)
    for i, e in enumerate(edges):
        for d in e:
            graph[i].append(d)

    print("The graph is:", graph)

    paths = find_all_paths(0, 4)
    print("All paths are", paths)
