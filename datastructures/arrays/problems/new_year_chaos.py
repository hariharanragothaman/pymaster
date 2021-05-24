"""
https://www.hackerrank.com/challenges/new-year-chaos
"""

def find_min_bribes(arr):
    n = len(arr)
    bribes = 0
    for i in range(n-1, -1, -1):
        if arr[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, arr[i]-2), i):
            if arr[j] > arr[i]:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    q = list(map(int, input().split()))
    find_min_bribes(q)