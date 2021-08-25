def solve(s):
    """This gets substring of length 2 - can be extrapolated to others"""
    n = len(s)
    for length in range(2, 3):
        for i in range(0, n - length + 1):
            sub_str = s[i : i + length]
            print(sub_str)
