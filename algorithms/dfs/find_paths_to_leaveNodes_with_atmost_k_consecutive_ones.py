from collections import defaultdict

vertices, threshold = map(int, input().split())
# Truth table
arr = [0] + list(map(int, input().split()))
g = defaultdict(list)
i = 0
while i < vertices - 1:
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    i += 1

# Actual solution begins here...
# paths(1, arr, g, threshold)

q = [(1, 0, 0)]
cnt = 0

while q:
    k, c, p = q.pop()
    c = arr[k] * (c+1)
    if c > threshold:
        continue
    if len(g[k]) == 1 and k != 1:
        cnt += 1
        continue

    for children in g[k]:
        if children != p:
            q.append([children, c, k])

print(cnt)