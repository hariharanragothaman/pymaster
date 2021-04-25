"""
Given a graph, find all paths from source to target
"""
from collections import defaultdict


def find_all_paths(start, end, path=[]):
    """
    Args:
        start: Starting destination
        end: End Destination
        path: Initial path - []
    Returns: returns all_paths, list of lists
    """
    # Container to store the result
    all_paths = []

    # This line is creating each path, and start changes during every recursion call
    path = path + [start]
    # print(f"The all paths are {all_paths}")
    # print("The path is: ", path)

    # When you reach the end of one full-path, that is returned
    if start == end:
        return [path]

    for node in graph[start]:
        # print("The node is ", node)
        if node not in path:
            new_paths = find_all_paths(node, end, path)
            # print(f"The new paths is {new_paths}")
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
    paths = find_all_paths(start=0, end=4)
    print("All paths are", paths)
