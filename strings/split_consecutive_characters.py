import itertools

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
    return ans


def split_into_same_char_segments_2(s):
    groups= []
    for _, v in itertools.groupby(s):
        groups.append(''.join(v))
    return groups

def split_into_same_char_segments_3(arr):
    """
    This helps in splitting the array and finding continuous subsegments smartly
    """
    temp = []
    n = len(arr)

    cnt, prev = 1, arr[0]
    for i in range(n - 1):
        if arr[i + 1] == prev:
            cnt += 1
        else:
            temp.append(cnt)
            cnt = 1
        prev = arr[i + 1]
    temp.append(cnt)
    return temp



if __name__ == '__main__':
    segments = split_into_same_char_segments("aaaabbbab")
    print(segments)

    segments2 = split_into_same_char_segments_2("aaaabbbab")
    print(segments2)
