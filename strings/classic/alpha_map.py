def alpha_map_count():
    alpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    num = list(range(1, 27))
    return dict(zip(alpha, num))


def alpha_map_bool():
    alpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    boolean = [False] * 26
    return dict(zip(alpha, boolean))


if __name__ == '__main__':
    print(alpha_map_count())
    print(alpha_map_bool())
