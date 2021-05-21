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



if __name__ == '__main__':
    arr = list(map(int, input().split()))
    find_min_swaps_to_sort(arr)