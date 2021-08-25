"""
The parity of a binary word is:

1 - if number of 1's is odd
0 - if number of 1's is even

- How would you compute for very large binary strings?
"""


def find_parity_using_string(n: int) -> int:
    str_n = str(n)
    if str_n.count("1") % 2 == 0:
        return 0
    return 1


if __name__ == "__main__":
    result = find_parity_using_string(10 ** 9 + 7)
    print(f"The result is: {result}")
