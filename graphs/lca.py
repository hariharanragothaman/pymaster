from collections import defaultdict

class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = [-1] * len(graph)
        P = [-1] * len(graph)
        t = -1
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path[t] = P[node]
            self.time[node] = t = t + 1
            for nei in graph[node]:
                if self.time[nei] == -1:
                    P[nei] = node
                    dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def __call__(self, a, b):
        if a == b:
            return a
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b)]

def lca_recursive(self, root, a, b):
    # Standard Recipe to find the lowest-common ancestor
    if root is None or root is a or root is b:
        return root
    left = self.lca(root.left, a, b)
    right = self.lca(root.right, a, b)
    if left is not None and right is not None:
        return root
    return left if left else right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root, ]
        parent_map = {root: None}

        while stack:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)

        if p not in parent_map or q not in parent_map:
            return None

        ancestors = set()
        while p :
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]
        return q


if __name__ == "__main__":
    g = {0: [1], 1: [2, 3, 4], 2: [5, 6], 3: [1], 4: [1, 7], 5: [2], 6: [2], 7: [4]}
    print("The graph is:", g)
    lca = LCA(1, g)
    result = lca(5, 6)
    print("The lowest common ancestor is:", result)
