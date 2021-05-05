
def count_if_all_digits_are_same(n):
    """
    Args:
        n: the range upto which we need to find numbers with the same digits
    Returns:

    """
    A = []
    for c in map(int, '123456789'):
        x = c
        while x < 10**9:
            A.append(x)
            x = 10 * x + c
    return A


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = count_if_all_digits_are_same(n)
        print (sum(1 for a in result if a <= n))