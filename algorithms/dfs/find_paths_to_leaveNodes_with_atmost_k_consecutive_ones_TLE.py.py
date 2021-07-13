from collections import defaultdict


def paths(root, arr, g, threshold):
    if not root:
        return []

    paths = []
    visited = set()

    stack = [(root, arr[root])]
    while stack:
        node, path = stack.pop()

        children = g[node]
        if len(children) == 1 and node != 1:
            paths.append(path)

        for c in children:
            if c not in visited:
                stack.append((c, str(path) + str(arr[c])))
                visited.add(c)

    cnt = 0

    for s in paths:
        tmp_cnt = mx_cnt = 0
        for i in range(len(s)):
            if s[i] == '1':
                tmp_cnt += 1
                mx_cnt = max(tmp_cnt, mx_cnt)
            elif s[i] == '0':
                mx_cnt = max(tmp_cnt, mx_cnt)
                tmp_cnt = 0
        if mx_cnt <= threshold:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    vertices, threshold = map(int, input().split())
    cats = [0] + list(map(int, input().split()))
    g = defaultdict(list)
    i = 0
    while i < vertices - 1:
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        i += 1
    paths(1, cats, g, threshold)