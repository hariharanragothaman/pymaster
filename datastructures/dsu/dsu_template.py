"""
This data-structure can help us group nodes into different sets.

Through this, we can eventually
1. Find number of connected components.
2. How many sets of connected components & find the connected components
3. Determine if there is a cycle in the graph

Future applications
1. Path-compression etc. - Makes sense. If we just know the representative, that's enough? Good point

"""


class DisJointSets:
    def __init__(self, size: int) -> None:
        self.parents = [-1 for _ in range(size)]
        self.sizes = [1 for _ in range(size)]

    def find(self, x: int):
        """Find the representative node in a's component"""
        if self.parents[x] == -1:
            return x
        # Oooh - This is a recursive call - We need to be careful here
        # Change to iterative potentially
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        """This also connects both 2 edges together - as in creates the graph itself"""
        """ Returns whether the merge changed connectivity"""
        x_root = self.find(x)
        y_root = self.find(y)

        # The connectivity has not changed
        if x_root == y_root:
            return False

        # Swappinpy for linking optimization
        if self.sizes[x_root] < self.sizes[y_root]:
            x_root, y_root = y_root, x_root
        self.parents[y_root] = x_root
        self.sizes[x_root] += self.sizes[y_root]
        return True


### Lets take a look at an example problem
"""
Initially We have an undirected graph with N vertices and 0 edges. Process the following Q queries in order:



I/P - The first line is N, Q - number of vertices and Q queries.
Each query is of the format (t, u, v)
if t == 0, Connect u and v - create a vertex b/w them
if t == 1 , tell if u and v are connected?  
    - In general we would have done DFS - but since this is in the form of queries 
      we need to use DSU 
"""


def solve():
    size, queries = list(map(int, input().split()))
    i = 0
    dsu = DisJointSets(size=size)
    while i < queries:
        t, u, v = list(map(int, input().split()))
        if t == 0:
            dsu.union(u, v)
        else:
            print(1 if dsu.find(u) == dsu.find(v) else 0)
        i += 1


######### Now Let's go in for a faster implementation #################


class DisjointSetUnionFast:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)
