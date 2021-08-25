import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
sys.setrecursionlimit(10 ** 7)


def get_nth_fibonacci(n):
    cache = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 2
    while i <= n:
        tmp = cache[-1]
        cache[-1] = cache[-1] + cache[-2]
        cache[-2] = tmp
        i += 1
    return cache[-1]


if __name__ == "__main__":
    n = int(input())
    res = get_nth_fibonacci(n)
    mod = 10 ** 9 + 7
    print(res % mod)
