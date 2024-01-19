"""
This can also be effectively used to see if there is a cycle in a directed graph
If there is a cycle in a directed graph -  the graph cannot be topologically sorted
Directed acyclic graph
"""


def topological_sort(graph):
    result = []
    visited = [0] * len(graph)

    # Creating 0 -> (n-1) nodes
    stack = list(range(len(graph)))

    while stack:
        node = stack.pop()
        if node < 0:
            result.append(~node)
        elif not visited[node]:
            visited[node] = 1
            stack.append(~node)
            stack += graph[node]

    # Cycle Check
    for node in result:
        if any(visited[nei] for nei in graph[node]):
            return None
        visited[node] = 0

    return result[::-1]


if __name__ == "__main__":
    g = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    result_sort = topological_sort(g)
    print("The topological sort is:", result_sort)
