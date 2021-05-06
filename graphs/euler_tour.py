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