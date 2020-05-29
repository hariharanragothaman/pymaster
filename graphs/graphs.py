# Fundamental templates for Graphs
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node, neighbour):
        self.graph[node].append(neighbour)
        """
        In terms of an un-directed graph - we would do:
        self.graph[node].append(neighbour)
        self.graph[neighbour].append(node)
        """
    # General strategy for BFS  - Works for undirected-graph
    def BFS(self, start):
        pass

    # General strategy for DFS - Works for undirected graph
    def DFS(self, start):
        pass

    # To find paths, given start and end
    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                return new_path
        return None

# Given edges check if there is a cycle

# Check if graph is bi-partite -- Graph Theory

# Check if graph is a Tree?

# Directed graph tricks