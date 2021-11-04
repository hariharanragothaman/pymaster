"""
Given a list of bad numbers, find the longest segment of good numbers within the given range

"""


def good_segment(bad_numbers, l, r):
    bad_numbers = [l - 1] + sorted(x for x in bad_numbers if l <= x <= r) + [r + 1]
    mx = 0
    for a, b in zip(bad_numbers, bad_numbers[1:]):
        gap = b - a
        mx = max(gap, mx)
    return mx - 1


if __name__ == "__main__":
    badNumbers = [37, 7, 22, 15, 49, 60]
    l = 3
    r = 48
    result = good_segment(badNumbers, l, r)
    print(result)
