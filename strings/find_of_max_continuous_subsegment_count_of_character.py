def get_count(self, s, char):
    n = len(s)
    max_count = 0
    tmp = 0
    for i in range(0, n):
        if s[i] == char:
            tmp += 1
        else:
            max_count = max(max_count, tmp)
            tmp = 0
    max_count = max(max_count, tmp)
    return max_count
