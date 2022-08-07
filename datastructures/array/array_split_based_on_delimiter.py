from itertools import groupby

tmp = ["10", "0", "1", "2", "0", "4", "5"]
chunks = (list(g) for k, g in groupby(tmp, key=lambda x: x != "0") if k)
res = [c for c in chunks]
print(*res)
