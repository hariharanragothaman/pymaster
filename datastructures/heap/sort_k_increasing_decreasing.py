import heapq
import itertools

A = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
print(A)


class Monotonic:
    def __init__(self):
        self._last = float('inf')

    def __call__(self, curr):
        result = curr < self._last
        self._last = curr
        return result


"""
The operation of groupby() is similar to the uniq filter in Unix. 
It generates a break or new group every time the value of the key function changes 
(which is why it is usually necessary to have sorted the data using the same key function)
"""
result = []

for is_decreasing, group in itertools.groupby(A, Monotonic()):
    print(is_decreasing, list(group))
    if is_decreasing:
        result.append(list(group)[::-1])
    else:
        result.append(list(group))

print("The result is:", result)

# Now call merge_sorted on result