# Check if 's' is a subsequence of 't'
# Method 1
def is_sub_sequence1(s, t):
    for i in range(len(s)):
        try:
            index = t.index(s)
        except ValueError:
            return False
        t = t[index + 1:]
    return True

# Method 2
def is_sub_sequence2(s, t):
    t = iter(t)
    return all(c in t for c in s)

# To generate all possible sub-strings - brute-force
strs = "Success"
for i in range(len(strs)):
    for j in range(i + 1, len(strs) + 1):
        print(strs[i:j])

# Longest Common Substring - given 2 strings
from difflib import SequenceMatcher
def find_length(A, B):
    if set(A).isdisjoint(B):
        return 0
    a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(0, len(A), 0, len(B))
    return size

def longest_increasing_subsequence():
    temp = []
    for n in arr:
        index = bisect.bisect_left(temp, n)
        if index == len(temp):
            temp.append(n)
        else:
            temp[index] = n
    return temp
