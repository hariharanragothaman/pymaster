"""
Nicer way to generate consecutive combinations in an array
(1,2), (2,3), (3,4), (4,5) --- from [1, 2, 3, 4, 5]
"""
arr = [1, 2, 3, 4, 5]

# Consecutive Combo of 1
for x, y in zip(arr, arr[1:]):
    print(x, y)


for x, y, z in zip(arr, arr[1:], arr[2:]):
    print(x, y, z)
