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


def get_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


def get_longest_palindrome_substring_optimized(s):
    lps = ""
    for i in range(len(s)):
        even = get_palindrome(s, i, i + 1)
        odd = get_palindrome(s, i, i)
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
        LPS[i] = (R > i) and min(R - i, LPS[2 * C - i]) # equals to i' = C - (i-C)

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


if __name__ == "__main__":
    s = input()
    result = manachers_algorithm(s)
    print(result)
