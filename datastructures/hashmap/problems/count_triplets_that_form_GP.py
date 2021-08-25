"""
Given an array, count triplets, that will form a geometric progression
"""

"""
Some GP fundae:
The nth term in GP is: a(n) = a * (r ** (n-1))
a(n) = r * (a(n-1))
r (common-ratio) = 
"""

from collections import Counter, defaultdict

"""
# Initial approach - that results in a TLE
def countTriplets(arr, r):
    ctr = Counter(arr)
    arr = sorted(set(arr))
    total = 0
    for i in range(len(arr)):
        b = r * arr[i]
        c = r * r * arr[i]
        if b in arr and c in arr:
            total += ctr[arr[i]] * ctr[b] * ctr[c]
    return total
"""


def count_triplets_that_form_gp(arr, r):

    v2 = defaultdict(int)
    # v3 is tracking how many end with a specific number
    v3 = defaultdict(int)

    total = 0

    for k in arr:
        total += v3[k]  # Increment the number of triplets that end with k
        v3[k * r] += v2[k]
        v2[k * r] += 1
        print(f"The total is: {total}")
        print(f"The v2 map is: {v2}")
        print(f"The v3 map is: {v3}")
        print("***********************")
    return total


if __name__ == "__main__":
    length, common_ratio = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = count_triplets_that_form_gp(arr, common_ratio)
    print("The result is:", result)
