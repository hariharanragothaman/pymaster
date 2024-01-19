def sort_by_value_then_key(H: dict) -> list:
    # To sort by value and then by key
    # Creates a tuple that are by default sorted by value, and then we set the priority
    ans = sorted(H, key=lambda x: (-H[x], x))
    return ans

def sort_map_by_priority_2(H: dict) -> list:
    """
    Another way to do it, store key-value pair as tuple in an array, then sort them
    2. We give max priority to x[1]
    3. If x[1] is the same then we give priority to x[0], but the '-' sign indicates the reverse order
    """
    A = [(k, v) for k, v in H.items()]
    A = sorted(A, key=lambda x: (x[1], -x[0]) )
    return A


if __name__ == '__main__':
    """
    Always remember - when you want to set multiple priorities - you need to create a tuple
    """
    A = [(2, 2), (-1, 1), (1, 1)]
    H = {2:2, -1:1, 1:1}
    H2 = {1: 50, 2: 25, 3: 45, 4: 100, 5: 10}

    ans1 = sort_map_by_priority_2(H)
    ans2 = sort_by_value_then_key(H)
    print(ans1)
    print(ans2)
