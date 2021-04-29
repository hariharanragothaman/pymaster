"""
Given a directed graph, check if it contains a cycle.

What's the real time application of this?

Imagine there is a deadlock detection in a system.
Processes can be determined by vertices a&
edge can be - Process is waiting for process B to release the mutex

There are 2 approaches to this:
1. Using color theory
2. Using powers of two
"""

# These example inputs can be generated using defaultdict
graph_with_cycle = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["F"],
    "D": ["E", "F"],
    "E": ["B"],
    "F": [],
}

graph_without_cycle = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["E"],
    "E": [],
    "F": [],
}

color_map = {"WHITE": 0, "GRAY": 1, "BLACK": 2}


def is_in_cycle(graph, states, vertex):
    if states[vertex] == color_map["GRAY"]:
        return True

    states[vertex] = color_map["GRAY"]

    for nei in graph[vertex]:
        if is_in_cycle(graph, states, nei):
            return True

    states[vertex] = color_map["BLACK"]
    return False


def contains_cycle(graph):
    states = {vertex: color_map["WHITE"] for vertex in graph}
    for vertex, state in states.items():
        if state == color_map["WHITE"] and is_in_cycle(graph, states, vertex):
            return True
    return False


# -----------------------------------------------------------------------------------------


if __name__ == "__main__":
    print(contains_cycle(graph_with_cycle))
    print(contains_cycle(graph_without_cycle))
