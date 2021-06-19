# Problem Reference: https://codeforces.com/contest/863/problem/B

"""
2n people

n-1 tandem kayaks and 2 single kayaks

weight = []

Property in tandem kayak is the abs difference
Property total = sum of property all boats

"""

from collections import Counter, defaultdict


def solve(weights, n):
    """
    This solution will not be accepted, but serves as a solid intuition
    """
    weights = sorted(weights)
    tandem_kayaks = n - 1
    single_kayak = 2
    # print(f"The weights are: {weights}")

    # First grouping all similar to reduce instability to zero
    ans = 0
    ctr = Counter(weights)
    for k, v in ctr.items():
        q, r = divmod(v, 2)
        ctr[k] = r

    # Now with the remaining ppl
    remaining = []
    for k, v in ctr.items():
        if v > 0:
            remaining += [k] * v
    # print("The remaining is:", remaining)

    hmap = defaultdict(int)
    for i in range(0, len(remaining) - 1):
        diff = abs(remaining[i] - remaining[i + 1])
        hmap[(i, i + 1)] = diff
    # print("The hmap is:", hmap)

    visited = set()
    hmap = {k: v for k, v in sorted(hmap.items(), key=lambda x: x[1])}
    # print("The hmap is:", hmap)

    rl = len(remaining)
    for k, v in hmap.items():
        a, b = k
        if rl <= 2:
            break
        if a not in visited and b not in visited:
            ans += v
            visited.add(a)
            visited.add(b)
            rl -= 2
            # print("The ans is:", ans)
            # print("The visited map is:", visited)
    print(ans)


def solve2(weights, n):
    """
    Here the focus is on removing the 2 weights - who will go in the single kayaks
    So for that we are generating all combinations and removing it
    with the result sorted array, we find the consecutive diff, and add them, and store it in a result.
    Finally we give - min of that result
    """
    from itertools import combinations
    from copy import deepcopy

    print(f"The I/P array is:", weights)

    result = []

    for c in combinations(weights, 2):  # Considering all combinations
        print("The combos are:", c)
        ls = deepcopy(weights)
        for j in c:
            print("The j is:", j)
            ls.remove(j)

        ls.sort()
        print(f"The sorted weights are: {ls}")
        ans = 0
        for i in range(0, (len(ls) - 1), 2):
            ans += abs(ls[i] - ls[i + 1])
        result.append(ans)
        print(f"The result is: {result}")
        print("****************************************")
    # print(f"The answer is: {result}")
    print(min(result))


if __name__ == "__main__":
    n = int(input())
    # weights = [1, 3, 4, 6, 3, 4, 100, 200]
    weights = list(map(int, input().split()))
    solve2(weights, n)
