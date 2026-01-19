"""
Given a directed graph, check if it contains a cycle.

What's the real time application of this?
    Imagine there is a deadlock detection in a system.
    Processes can be determined by vertices a& edge can be - Process is waiting for process B to release the mutex

There are 2 approaches to this:
1. Using color theory
2. Using powers of two
"""

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

#-------------------------------------------------------------------------------------------------------------------

# Brent's algorithm to detect cycles
def cycle_finding(f, x0):
    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length lam
    mu = 0
    tortoise = hare = x0
    for _ in range(lam):
        hare = f(hare)
    # The distance between the hare and tortoise is now lam.

    # Next, the hare and tortoise move at same speed until they agree
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam, mu

#-------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
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
    print(contains_cycle(graph_with_cycle))
    print(contains_cycle(graph_without_cycle))
