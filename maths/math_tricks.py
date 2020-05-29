from functools import reduce


# GCD and LCM of b/w 2 numbers
def gcd(a, b):
    while b != 0:
        a, b = a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


# To find all factors of a give number
def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


# 2D matrices Hacks
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[:] = zip(*matrix)  # Getting Transpose [ R->C, C->R ]
matrix[:] = zip(*matrix[::-1])  # Rotate a matrix - Transpose & reverse each row


# To get the rows of the matrix:
def get_rows(matrice):
    return [[c for c in r] for r in matrice]


def get_columns(matrice):
    return zip(*matrice)


# Reversing an integer
def reverse_integer(num):
    sign = -1 if num < 0 else 1
    result = 0
    x = abs(num)

    while x:
        # Getting the LSB-  multiply by 10 every time;
        # since it will be correct as we add digits
        result = (x % 10) + result * 10
        # Remove the LSB
        x = x // 10

    # Handle overflow bound scenario
    if x > 2 ** 31 + 1 or x < -2 ** 31 - 1:
        return 0

    return result * sign
