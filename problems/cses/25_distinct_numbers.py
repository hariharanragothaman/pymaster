import sys

input = sys.stdin.readline
n = int(input())
print(len(set(map(int, input().split()))))
