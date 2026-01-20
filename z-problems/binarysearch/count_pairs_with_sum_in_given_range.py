# Refer: https://codeforces.com/contest/1538/problem/C

from bisect import bisect_left


def solve2(arr, n, a, b):
    arr.sort()

    left = [0] * len(arr)
    right = [0] * len(arr)

    i, j = 0, len(arr) - 1
    while i - j <= 0:
        if arr[i] + arr[j] >= a:
            left[j] = i
            j -= 1
        else:
            left[i] = j + 1
            i += 1

    i, j = 0, len(arr) - 1
    while i - j <= 0:
        if arr[i] + arr[j] <= b:
            right[i] = j
            i += 1
        else:
            right[j] = i - 1
            j -= 1

    answer = [b - a + 1 - (a <= i <= b) for i, (a, b) in enumerate(zip(left, right))]
    return sum(answer) // 2


def solve(arr, n, a, b):
    arr.sort()
    result = 0
    # print("The array is:", arr)
    for i in range(n):
        val = a - arr[i]
        # print("The value is ", val)
        idx = bisect_left(arr, val, i + 1, n)
        # print("The idx is:", idx)
        # print("***************")
        for j in range(idx, n):
            if arr[j] + arr[i] <= b:
                result += 1
    return result


if __name__ == "__main__":
    t = int(input())
    i = 0
    while i < t:
        n, l, r = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        res = solve2(arr, n, l, r)
        print(res)
        i += 1
