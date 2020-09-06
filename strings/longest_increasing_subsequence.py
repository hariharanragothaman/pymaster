def longest_increasing_subsequence():
    temp = []
    for n in arr:
        index = bisect.bisect_left(temp, n)
        if index == len(temp):
            temp.append(n)
        else:
            temp[index] = n
    return temp
