# Check if 's' is a subsequence of 't'
# Method 1
def is_sub_sequence1(s, t):
    for i in range(len(s)):
        try:
            index = t.index(s)
        except ValueError:
            return False
        t = t[index + 1 :]
    return True


# Method 2
def is_sub_sequence2(s, t):
    t = iter(t)
    return all(c in t for c in s)
