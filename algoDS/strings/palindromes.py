from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def check_if_palindrome_can_be_formed(s):
    return sum(v % 2 == 1 for v in Counter(s).values()) <= 1

def reorder_string_to_form_palindrome(s):
    n = len(s)
    ctr = Counter(s)
    ctr = {k: v for k, v in sorted(ctr.items(), key=lambda x: x[1], reverse=True)}

    # If there is more than one odd value in the count of letters - palindrome cannot be formed
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



def get_longest_palindrome_substring(s):
    lps = ""
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(lps) > j - i:
                break
            elif s[i:j] == s[i:j][::-1]:
                lps = s[i:j]
                break
    return lps


def get_palindrome_from_string(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


def get_longest_palindrome_substring_optimized(s):
    lps = ""
    for i in range(len(s)):
        even = get_palindrome_from_string(s, i, i + 1)
        odd = get_palindrome_from_string(s, i, i)
        lps = max([lps, even, odd], key=lambda x: len(x))
    return lps


# best Case algorithm
def manachers_algorithm(s):
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = "#".join("^{}$".format(s))
    n = len(T)
    LPS = [0] * n
    C = R = 0

    for i in range(1, n - 1):
        LPS[i] = (R > i) and min(R - i, LPS[2 * C - i])  # equals to i' = C - (i-C)

        # Attempt to expand palindrome centered around i
        while T[i + 1 + LPS[i]] == T[i - 1 - LPS[i]]:
            LPS[i] += 1

        # if Palindrome centered around i expand past R,
        # adjust center based on expanded palindrome
        if i + LPS[i] > R:
            C, R = i, i + LPS[i]

    # Find max element in LPS
    max_length, center_index = max((n, i) for i, n in enumerate(LPS))
    return s[(center_index - max_length) // 2 : (center_index + max_length) // 2]
