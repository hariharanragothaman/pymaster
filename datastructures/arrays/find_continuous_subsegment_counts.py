def find_continuous_subsegment(arr):
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