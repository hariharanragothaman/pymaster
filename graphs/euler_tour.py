"""

"""

"""
Some basic concepts

1. A Eulerian path is a path in a graph that passes through all of its edges exactly once. 
2. A Eulerian cycle is a Eulerian path that is a cycle.

An Eulerian cycle exists if and only if the degrees of all vertices are even
And an Eulerian path exists if and only if the number of vertices with odd degrees is two 
    (or zero, in the case of the existence of a Eulerian cycle)
In addition, of course, the graph must be sufficiently connected 
    (i.e., if you remove all isolated vertices from it, you should get a connected graph).

The find the Eulerian path / Eulerian cycle we can use the following strategy: 

1. We find all simple cycles and combine them into one - this will be the Eulerian cycle. 
2. If the graph is such that the Eulerian path is not a cycle, 
        then add the missing edge, find the Eulerian cycle, then remove the extra edge.


"""
def euler_walk(n, adj):
    print("Entering here...")
    deg = [0] * n

    for i in range(n):
        for j in range(n):
            deg[i] += adj[i][j]

    print(deg)
    first = 0
    while deg[first] == 0:
        first += 1

    v1, v2 = -1, -1
    bad = False

    for i in range(n):
        if deg[i] % 2 == 1:
            if v1 == -1:
                v1 = i
            elif v2 == -1:
                v2 = i
            else:
                bad = True 
    print(bad)

    if v1 != -1:
        adj[v1][v2] += 1
        adj[v2][v1] += 1

    st, res = [first], []

    while st:
        v = st[-1]
        flag = False

        for i in range(n):
            if adj[v][i]:
                flag = True
                break

        if flag:
            adj[v][i] -= 1
            adj[i][v] -= 1
            st.append(i)
        else:
            res.append(v)
            st.pop()

    print("Outside while loopp")
    if v1 != -1:
        for i in range(len(res) - 1):
            if ((res[i] == v1) and (res[i + 1] == v2)) or ((res[i] == v2) and (res[i + 1] == v1)):
                res = [res[j] for j in range(i + 1, len(res))] + [res[j] for j in range(1, i + 1)]
                break

    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                bad = True

    if bad:
        return None
    print(res)
    return res

if __name__ == '__main__':
    f = [2,2,1,2]
    n = len(f)
    g = []
    for i in range(n):
        g.append([0]*n)
    print(g)
    
    for i, c in enumerate(f):
        g[i][c] = 1
    
    print(g)
    euler_walk(n, g)