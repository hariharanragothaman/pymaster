def is_palindrome(s):
    def mirror(i):
        return -(i + 1)

    for i in range(len(s) / 2):
        if s[mirror(i) != s[i]]:
            return False
    return True
