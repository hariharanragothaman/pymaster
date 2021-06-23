from collections import defaultdict, deque


def find_tree_diameter(g, n):
    """
    Standard awesome problem
    So for each node, I want to find the maximum distance to another node
    :param g:
    :return:
    """
    # We can approach this question in the binary tree way (or) the graph way
    # Tree - Post order traversal - This in itself is DFS template only
    # Graph - Use routine DFS - Remember - tree is an undirected graph

    diameter_of_tree = 0

    for i in range(1, n+1):
        print(f"Considering {i} as root")
        curr_max_length = 0
        q = deque()
        q.append((i, 0))
        visited = set()

        while q:
            print("The queue is:", q)
            node, length = q.pop()
            visited.add(node)
            curr_max_length = max(length, curr_max_length)

            for nei in g[node]:
                if nei not in visited:
                    q.append((nei, length+1))

        print(f"The max_length for {i} is: {curr_max_length}")
        diameter_of_tree = max(curr_max_length, diameter_of_tree)
        print("*****************************************************")

    return diameter_of_tree

if __name__ == '__main__':
    n = int(input())
    g = defaultdict(list)
    for i in range(0, n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    # print(g)
    result  = find_tree_diameter(g, n)
    print(result)