A = [[1, 2, 3, 4, 5], [7, 2, 3, 4, 5]]
print(A)

g = [iter(x) for x in A]
print(g)

for i, it in enumerate(g):
    print(i, it)
    f = next(it, None)
    print(f)
    print("-" * 10)
