import sys

n = int(sys.stdin.buffer.readline())
print(len(set(map(int, sys.stdin.buffer.readline().split()))))
