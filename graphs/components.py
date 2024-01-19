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

def count_components(n,  g) -> int:
    visited = [False] * n
    count = 0

    for i in range(n):
        # Core Logic is: = If it's already visited - then it means it's already connected to something
        if visited[i]:
            continue
        else:
            count += 1

        stack = [i]
        while stack:
            node = stack.pop()
            for nei in g[node]:
                if not visited[nei]:
                    # If it's a neighbor, you can visit through this node
                    visited[nei] = True
                    stack.append(nei)

    return count


if __name__ == "__main__":
    # Defining the Graph
    vertices = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    result = count_components(vertices, graph)
    print(result)

    components = connected_components(vertices, graph)
    print(f"The Components are: {components}")
