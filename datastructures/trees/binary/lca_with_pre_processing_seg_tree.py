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
        return self.func(
            self._data[depth][begin], self._data[depth][end - (1 << depth)]
        )


class LCA:
    def __init__(self, root, graph):
        """Assumes the graph is zero-indexed"""

        self.first = [-1] * len(graph)
        self.path = [-1] * len(graph)
        parents = [-1] * len(graph)
        h = -1

        dfs = [root]

        # This is just routine-standard DFS traversal
        while dfs:
            print("The dfs is:", dfs)
            node = dfs.pop()
            print("The node popped is:", node)
            self.path[h] = parents[node]
            self.first[node] = h = h + 1
            for nei in graph[node]:
                if self.first[nei] == -1:
                    parents[nei] = node
                    dfs.append(nei)

            print("The parents array is:", parents)
            print("The first array:", self.first)
            print("The path is:", self.path)
            print("****************************************************************")

        heights = [self.first[node] for node in self.path]
        print("The heights are:", heights)
        # Instantiating the rangeQuery class with heights
        self.rmq = RangeQuery(heights)

    def __call__(self, left, right):
        if left == right:
            return left

        # The first array is storing the heights
        left = self.first[left]
        right = self.first[right]

        # If left is greater than right
        if left > right:
            left, right = right, left

        return self.path[self.rmq.query(left, right)]


if __name__ == "__main__":
    g = {0: [1], 1: [2, 3, 4], 2: [5, 6], 3: [1], 4: [1, 7], 5: [2], 6: [2], 7: [4]}
    print("The graph is:", g)
    lca = LCA(1, g)
    result = lca(5, 6)
    print("The lowest common ancestor is:", result)
