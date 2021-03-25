"""
A number is strobogrammatic if the number looks the same, when rotate by 180 degrees,
upside down
"""

def is_strobogrammatic(num)-> bool:
    """
    It has to be palindromic stylish and we should also be able to swap / interchange.
    That's the intuition
    Args:
        num:
    Returns:
    """
    comb = '00 11 88 69 96'
    i, j = 0, len(num) - 1
    while i <= j:
        x = comb.split(num[i]+num[j])
        if x == -1:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    s = "11"
    is_strobogrammatic(s)