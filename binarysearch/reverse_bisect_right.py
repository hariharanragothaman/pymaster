# This is to apply bisect right in reverse sorted array
def reverse_bisect(scores, value):
    low, high = 0, len(scores)
    while low < high:
        mid = (low + high) // 2
        if value > scores[mid]:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    arr = [5, 4, 2, 2, 1, 0]
    op = reverse_bisect(arr, 3)
    print(op) 