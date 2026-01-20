from collections import deque

def bfs(graph, start=0):
    length = len(graph) + 1 if start == 1 else len(graph)
    used = [False] * length
    used[start] = True
    q = [start]
    for v in q:
        for w in graph[v]:
            if not used[w]:
                used[w] = True
                q.append(w)


def layers(graph, start=0):
    length = len(graph) + 1 if start == 1 else len(graph)
    used = [False] * length
    used[start] = True
    q, ret = [start], []
    while q:
        nq = []
        ret.append(q)
        for v in q:
            for w in graph[v]:
                if not used[w]:
                    used[w] = True
                    nq.append(w)
        q = nq
    return ret

def layers2(graph, start):
    level, level_order = 0, []
    visited = {}
    for k in graph:
        visited[k] = False

    q = deque([start])
    while q:
        level_order.append([])
        for i in range(len(q)):
            vertex = q.popleft()
            for neighbours in graph[vertex]:
                if not visited[neighbours]:
                    visited[neighbours] = True
                    q.append(neighbours)
            level_order[level].append(vertex)
        level += 1
    return level_order

if __name__ == '__main__':
    """
    If it is directed graph, then vertex will exist as 'key', value is empty list
    if it's undirected graph, then there will bi-directional connections
    """
    G = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4:[], 5:[], 6:[], 7:[]}

    layers = layers(G, start=1)
    print(layers)

    # Calling usual BFS recipe
    levels = layers2(G, start=1)
    print(levels)
