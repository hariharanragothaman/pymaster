def bfs(graph, start=0):
    visited = [False] * len(graph)
    visited[start] = True

    q = [start]
    for v in q:
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)


def layers(graph, start=0):
    visited = [False] * len(graph)
    visited[start] = True
    q, result = [start], []
    while q:
        nq = []
        result.append(q)
        for v in q:
            for w in graph[v]:
                visited[w] = True
                nq.append(w)
        q = nq
    return result
