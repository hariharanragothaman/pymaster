def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    s = "madam"
    ans1 = is_palindrome(s)
    print(ans1)
    s = "helloo"
    ans1 = is_palindrome(s)
    print(ans1)
