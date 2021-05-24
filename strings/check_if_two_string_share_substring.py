"""
Problem Ref:
https://www.hackerrank.com/challenges/two-strings/
"""


def check_for_common_substring(s1, s2):
    return 'YES' if set(list(s1)) & set(list(s2)) != set() else 'NO'


if __name__ == '__main__':
    s1, s2 = 'and', 'art'
    ss1, ss2 = 'be', 'dog'
    check_for_common_substring(s1, s2)