"""
Given a string - reorder it to from palindrome
"""

from collections import Counter


def check_if_palindrome_can_be_formed(s):
    return sum(v % 2 for k, v in Counter(s).items()) <= 1


def palindrome_reorder(s):
    # Check if palindrome can be formed
    n = len(s)
    ctr = Counter(s)
    ctr = {k: v for k, v in sorted(ctr.items(), key=lambda x: x[1], reverse=True)}
    # print(ctr)

    # If there is more that one odd value in the count of letters - palindrome cannot be formed
    odd_count = 0
    for v in ctr.values():
        if v & 1:
            odd_count += 1
    if odd_count > 1:
        return "NO SOLUTION"

    # now going individually for odd and even cases

    if n & 1:
        # The length of the string is odd
        op = pivot = ""
        middle = ""

        # Finding the pivot:
        for k, v in ctr.items():
            if v % 2 != 0:
                middle = k * v
                pivot = k

        for k, v in ctr.items():
            if k != pivot:
                op += k * (v // 2)
        return op + middle + op[::-1]

    else:
        # The length of the string is even
        op = ""
        for k, v in ctr.items():
            op += k * (v // 2)
        return op + op[::-1]


if __name__ == "__main__":
    s = input()
    res = palindrome_reorder(s)
    print(res)
