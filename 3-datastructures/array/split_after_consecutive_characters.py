def split_into_same_char_segments(s):
    n, ans, ch = len(s), [], ""

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ch += s[i]
        elif s[i] != s[i + 1]:
            ch += s[i]
            ans.append(ch)
            ch = ""
    if ch:
        ch += s[-1]
        ans.append(ch)
    else:
        ans.append(s[-1])
    print(ans)

if __name__ == '__main__':
    split_into_same_char_segments("aaaabbbab")
