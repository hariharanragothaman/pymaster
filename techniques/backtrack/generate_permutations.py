"""
File focuses on generating permutations:

Given a collection of distinct numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
Generate permutations - The classic DFS way
"""
def generate_permutations(arr):
    result = []
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    for i in range(len(arr)):
        extract = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in generate_permutations(remaining):
            result.append(p + [extract])
    return result


"""
Generate permutations by yield an iterator.
"""
def gen_permute_iter(arr):
    if len(arr) < 1:
        yield arr
    else:
        for perm in gen_permute_iter(arr[1:])
            for i in range(len(arr)):
                yield perm[:i] + arr[0:1] + perm[i:]

if __name__ == '__main__':
    nums = [1, 2, 3]
    op = generate_permutations(nums)
    print("The op is:", op)