"""
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in the array.
"""


def find_max(arr, queries):
    for l, r, value in queries:
        for idx in range(l, r + 1):
            arr[idx] += value
    return max(arr)

# To optimize this:- Another approach is to use lazy propogation of Segment Tree as well.


def array_manipulation(n, queries):
    # Write your code here
    array = [0] * (n + 1)

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        print(f"The array is: {array}")

    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count

    return max_value


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = [0] * n
    i = 0
    queries = []
    while i < m:
        a, b, val = list(map(int, input().split()))
        q = queries.append((a-1, b-1, val))
        i += 1
    find_max(arr, queries)