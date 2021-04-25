from collections import defaultdict
from collections import deque

def connected_components(graph, n):
    """
    Vertices start from 0.. n
    """
    overall = set()
    start = 0
    while start < vertices:
        visited = {}
        rpath = []

        for k in graph:
            visited[k] = False

        q = deque([start])
        visited[start] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
            rpath.append(node)
        overall.add(tuple(sorted(rpath)))
        start += 1

    return overall

if __name__ == '__main__':
    vertices, edges = list(map(int, input().split()))
    graph = defaultdict(list)
    i = 0
    while i < edges:
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        i += 1
    print(graph)

    # Getting the connected components
    _components = connected_components(graph, vertices)
    print("The connected components are:", _components)
