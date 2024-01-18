import functools


def string_hash(s, mod):
    mult = 997
    return functools.reduce(lambda v, c: ((v * mult) + ord(c)) % mod, s, 0)


s = "codeforces"
res = string_hash(s, 11)
print(res)
