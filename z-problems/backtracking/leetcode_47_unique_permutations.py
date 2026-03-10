"""
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def generate_unique_permute(arr):
    """
    The go-to can also putting them in a set when generating all permutations
    Now, lets look into a smarter way of doing this.
    """
    result = [[]]
    for n in arr:
        temp = []
        for l in result:
            for i in range(len(l) + 1):
                temp.append(l[:i] + [n] + l[i:])
                if i < len(l) and l[i] == n:
                    break
        result = temp
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    op = generate_unique_permute(nums)
    print(op)
