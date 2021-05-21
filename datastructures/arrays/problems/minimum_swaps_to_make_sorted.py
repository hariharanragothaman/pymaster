def find_min_swaps_to_sort(arr):
    """ This solution TLE'ed - we need to optimize this"""
    start = 1
    end = len(arr)

    i = 0
    while start <= end:
        print(f"The arr is: {arr}")
        if arr[start-1] == start:
            start += 1
            continue
        else:
            idx = arr.index(start)
            arr[idx], arr[start-1] = arr[start-1], arr[idx]
            i += 1
            start += 1
    print(i)

def find_min_swaps_to_sort_slightly_optimized(arr):
    """ This solution TLE'ed - we need to optimize this"""
    start = 1
    end = len(arr)

    hmap = {}
    for i, val in enumerate(arr):
        hmap[val] = i

    i = 0
    while start <= end:
        if arr[start-1] != start:
            idx = hmap[start]
            arr[idx], arr[start-1] = arr[start-1], arr[idx]

            # Updating the hashmap as well - which is like our database
            hmap[arr[idx]] = idx
            hmap[arr[start-1]] = start-1


            i += 1
        start += 1
    print(i)

# This is TLE'ing I guess because of finding the index of it() - Oh! interesting


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    find_min_swaps_to_sort_slightly_optimized(arr)