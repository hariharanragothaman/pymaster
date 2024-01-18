import bisect

def is_sub_sequence1(s, t):
    # Check if 's' is a subsequence of 't'
    for i in range(len(s)):
        try:
            index = t.index(s[i])
        except ValueError:
            return False
        t = t[index + 1 :]
    return True

def is_sub_sequence2(s, t):
    # Check if 's' is a subsequence of 't'
    t = iter(t)
    return all(c in t for c in s)

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

def longestCommonSubsequence(self, a: str, b: str) -> int:
    lengths = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    result = []
    x, y = len(a), len(b)

    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            result.append(a[x - 1])
            x -= 1
            y -= 1

    return len(result)



if __name__ == "__main__":
    arr = [7, 3, 5, 3, 6, 2, 9, 8]
    print(f"The I/P array is: {arr}")
    result = longest_increasing_subsequence(arr)
    print(result)
