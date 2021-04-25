
from collections import defaultdict


def find_path(start, end, parents):
    """Constructs a path from given starting index to end index"""
    path, parent = [], end

    while parent != parents[start]:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]

if __name__ == '__main__':

    # Creating a graph with key as node and value as parents
    g = defaultdict()
    g[1] = 0
    g[2] = 1
    g[3] = 1
    g[4] = 2
    g[5] = 2
    g[6] = 3
    g[7] = 2
    g[8] = 5
    print(g)
    result = find_path(1, 8, g)
    print("The result is:", result)