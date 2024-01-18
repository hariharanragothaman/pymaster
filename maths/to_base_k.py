def to_base_k(self, n: int, k: int) -> str:
    res = []
    while n:
        n, rem = divmod(n, k)
        res.append(rem)
    res = res[::-1]
    res = ''.join(str(c) for c in res)
    return res
