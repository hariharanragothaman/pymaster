def myPow(x, n, m):
    if n == 0:
        return 1
    if n % 2 == 0:
        return myPow((x * x) % m, n / 2, m)
    return x * myPow(x, n - 1, m) % m
