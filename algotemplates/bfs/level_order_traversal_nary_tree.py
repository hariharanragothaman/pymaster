from collections import deque


def level_order_traversal_nary_tree(graph, start):
    """
    Basically we have to level-order-traversal of an n-array tree
    :param graph:
    :return:
    """
    q = deque([start])

    traverse = []
    level = 0

    while q:
        traverse.append([])
        for i in range(len(q)):
            node = q.popleft()
            traverse[level].append(node)
            for nei in graph[node]:
                q.append(nei)

        level += 1
    print(traverse)
    print(len(traverse))
