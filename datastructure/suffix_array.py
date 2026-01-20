from collections import defaultdict

"""
Let s be a string of length n
The ith suffix of s is the sub-string s [i..n-1]

The suffix array will contain integers that represent the starting index of the all the suffixes

s = "abaab"

All the suffixes are:
 0 - abaab
 1 - baab
 2 - aab
 3 - ab
 4 - b

 After sorting them

 2 - aab
 3 - ab
 0 - abaab
 4 - b
 1 - baab

 Suffix array will be - (2, 3, 0, 4, 1)

 Things covered:
 1. Construction of a Suffix array
 2. Applications
"""


def build_suffix_array_naive(s):
    """n**2 (log(n))"""
    suffixes = []
    for i in range(len(s)):
        suffixes.append(s[i:])
    print("The suffixes are:", suffixes)
    hmap = defaultdict(int)
    for i, c in enumerate(suffixes):
        hmap[c] = i
    print("The hashmap is:", hmap)
    sorted_suffixes = sorted(suffixes)
    print(sorted_suffixes)

    sufffix_array_result = []
    for c in sorted_suffixes:
        sufffix_array_result.append(hmap[c])
    return sufffix_array_result


def build_suffix_array_naive_better(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

def SAIS(A):
    """
    Calculates suffix array in O(len(A) + max(A))
    Input:
    Int list A with A[i] >= 0 for all i
    """
    n = len(A)
    buckets = [0] * (max(A) + 2)
    for a in A:
        buckets[a + 1] += 1
    for b in range(1, len(buckets)):
        buckets[b] += buckets[b - 1]
    isL = [1] * n
    for i in reversed(range(n - 1)):
        isL[i] = +(A[i] > A[i + 1]) if A[i] != A[i + 1] else isL[i + 1]

    def induced_sort(LMS):
        SA = [-1] * (n)
        SA.append(n)
        endpoint = buckets[1:]
        for j in reversed(LMS):
            endpoint[A[j]] -= 1
            SA[endpoint[A[j]]] = j
        startpoint = buckets[:-1]
        for i in range(-1, n):
            j = SA[i] - 1
            if j >= 0 and isL[j]:
                SA[startpoint[A[j]]] = j
                startpoint[A[j]] += 1
        SA.pop()
        endpoint = buckets[1:]
        for i in reversed(range(n)):
            j = SA[i] - 1
            if j >= 0 and not isL[j]:
                endpoint[A[j]] -= 1
                SA[endpoint[A[j]]] = j
        return SA

    isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
    isLMS.append(1)
    LMS = [i for i in range(n) if isLMS[i]]
    if len(LMS) > 1:
        SA = induced_sort(LMS)
        LMS2 = [i for i in SA if isLMS[i]]
        prev = -1
        j = 0
        for i in LMS2:
            i1 = prev
            i2 = i
            while prev >= 0 and A[i1] == A[i2]:
                i1 += 1
                i2 += 1
                if isLMS[i1] or isLMS[i2]:
                    j -= isLMS[i1] and isLMS[i2]
                    break
            j += 1
            prev = i
            SA[i] = j
        LMS = [LMS[i] for i in SAIS([SA[i] for i in LMS])]
    return induced_sort(LMS)


if __name__ == "__main__":
    s = "abaab"
    tmp = [ord(c) for c in s]
    suffix_array = SAIS(tmp)
    print(suffix_array)

    suffix_array = build_suffix_array_naive_better(s)
    print(suffix_array)
