"""
Count number of bits that are set to 1 in a non-negative integer
"""


def count_bits_set_to_one(n) -> int:
    """
    x << y # Shift to left by y bits -- x * (2**y)
    x >> y  # Shift to right by y bits -- x // (2**y)
    Args:
        n: The I/P number
    Returns:

    Logic: And with 1 , and keep dividing n by powers of 2
    """
    num_bits = 0
    while n:
        num_bits += n & 1
        n = n >> 1
        print("n is:", n)
    return num_bits


if __name__ == '__main__':
    n = int(input())
    result = count_bits_set_to_one(n)
    print(f"The number of bits is: {result}")