from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.number_of_nodes = 10

    def build_graph(self):
        # Build the default dict here
        pass

    def dfs_check(self):
        visited = {}
        start = "0"

        # Mark all visited to False initially
        for k in range(self.number_of_nodes):
            visited[str(k)] = False
        print(f"The initial visited is: {visited}")

        q = deque(start)
        visited[start] = True

        # Starting DFS recipe
        while q:
            node = q.pop()
            for nei in self.g[node]:
                if visited[nei] == False:
                    visited[nei] = True
                    q.append(nei)

        if all(c for c in list(visited.values())):
            return True
        return False
