def bin_number(n, size=4):
    return bin(n)[2:].zfill(size)


def iar():
    return list(map(int, input().split()))


def ini():
    return int(input())


def isp():
    return map(int, input().split())


def sti():
    return str(input())


def par(a):
    print(' '.join(list(map(str, a))))


def tdl(outerListSize, innerListSize, defaultValue=0):
    return [[defaultValue] * innerListSize for i in range(outerListSize)]


def sts(s):
    s = list(s)
    s.sort()
    return ''.join(s)


def bis(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return [i, True]
    else:
        return [-1, False]


class pair:
    def __init__(self, f, s):
        self.fi = f
        self.se = s

    def __lt__(self, other):
        return (self.fi, self.se) < (other.fi, other.se)


# Getting a list of integers space seperated
def int_list():
    return list(map(int, input().split()))


def read_till_end():
    return sys.stdin.read().split()


def just_read():
    return sys.stdin.readline()


if __name__ == '__main__':
    values = int_list()
    print(*values)
