res = [1, 2, 3, 4, 5]
hmap = {1: 50, 2: 25, 3: 45, 4: 100, 5: 10}

print(res)
print(hmap)

res = sorted(res, key=lambda x: hmap[x], reverse=True)
print(res)
