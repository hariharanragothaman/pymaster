from collections import defaultdict


def connected_components(n, graph):
    components, visited = [], [False] * n

    def dfs(start):
        component, stack = [], [start]

        while stack:
            start = stack[-1]

            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True
                component.append(start)

            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)

        return component

    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))

    return components


if __name__ == "__main__":
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
