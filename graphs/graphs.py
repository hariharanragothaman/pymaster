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
        visited = {}
        result_path = []
        for k in self.graph:
            visited[k] = False

        q = deque(start)
        while q:
            vertex = q.popleft()
            for neighbours in self.graph[vertex]:
                if visited[neighbours] is False:
                    visited[neighbours] = True
                    q.append(neighbours)
            result_path.append(vertex)
        return result_path

    # General strategy for DFS - Works for undirected graph
    def DFS(self, start):
        visited = {}
        result_path = []
        for k in self.graph:
            visited[k] = False

        stack = [start, ]
        visited[start] = True

        q= deque(start)
        while q:
            vertex = q.popleft()
            for neighbours in self.graph[vertex]:
                if visited[neighbours] is False:
                    stack.append(neighbours)
        return result_path

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

    # Template to find all paths
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return None
        paths = []

        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for np in new_paths:
                    paths.append(np)
        return paths