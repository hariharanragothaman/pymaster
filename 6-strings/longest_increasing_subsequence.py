import bisect


def longest_increasing_subsequence(arr):
    temp = []
    for n in arr:
        index = bisect.bisect_left(temp, n)
        if index == len(temp):
            temp.append(n)
        else:
            temp[index] = n
        print(f"The temp is: {temp}")
    return temp


if __name__ == "__main__":
    arr = [7, 3, 5, 3, 6, 2, 9, 8]
    print(f"The I/P array is: {arr}")
    result = longest_increasing_subsequence(arr)
    print(result)
