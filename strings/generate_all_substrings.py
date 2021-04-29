# To generate all possible sub-strings - brute-force

s = "Success"
for left in range(len(s)):
    for right in range(left, len(s)):
        substring = s[left : right + 1]
        print(substring)
