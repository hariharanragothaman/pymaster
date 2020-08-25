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