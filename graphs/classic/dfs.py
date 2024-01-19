from collections import deque

def dfs(graph, start=0):
    n = len(graph) + 1 if start == 1 else len(graph)
    dp = [0] * n
    visited, finished = [False] * n, [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()

            # base case
            dp[start] += 1

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return visited, dp

def DFS(graph, start):
    visited = {}
    result_path = []
    for k in graph:
        visited[k] = False

    stack = [start]
    visited[start] = True

    q = deque([start])
    while q:
        vertex = q.pop()
        for neighbours in graph[vertex]:
            if visited[neighbours] is False:
                stack.append(neighbours)
    return result_path

if __name__ == '__main__':
    """
    If it is directed graph, then vertex will exist as 'key', value is empty list
    if it's undirected graph, then there will bi-directional connections
    """
    G = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4:[], 5:[], 6:[], 7:[]}
    dfs_path = DFS(G, 1)
    print(dfs_path)

    result = dfs(G, start=1)
    print(result)
