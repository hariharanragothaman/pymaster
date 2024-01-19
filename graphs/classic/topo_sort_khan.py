"""
Welcome to the concept of in-degree and out-degree
It's the longest path from in-degree (0) to out-degree (0)

Step1: Compute the in-degree for each vertex present in DAG
       Initialize count of visited nodes as zzero

Step2: Pick all vertexes with indegree of zero and add them to the Queue

Step3: Remove the vertex from the queue
       Increment visited count by 1
       decrease in-degree() by 1 for all it's neighbours(popped node reference)

Repeat Step3 until queue is empty.
"""


def khan(graph):
    n = len(graph)
    in_degree = [0] * n
    idx = [0] * n

    for i in range(n):
        for edge in graph[i]:
            in_degree[edge] += 1

    print("The indegree is:", in_degree)

    q = []
    topo_sort = []

    # Adding all elements with in-degree zero into the queue
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    nr = 0

    while q:
        node = q.pop()
        topo_sort.append(node)

        idx[topo_sort[-1]], nr = nr, nr + 1

        # Reducing the in-degree
        for edge in graph[topo_sort[-1]]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                q.append(edge)

    return topo_sort, idx, nr == n


if __name__ == "__main__":
    g = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    result_sort = khan(g)
    print("The topological sort is:", result_sort)
