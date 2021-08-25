# For example lets say we need 7 decimal points after calculating something

n = int(input())
s = list(map(int, input().split()))
ans = sum(s) / n
print("%.7f" % ans)
