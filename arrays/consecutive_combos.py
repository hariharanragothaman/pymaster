"""
Nicer way to generate consecutive combinations in an array
"""
arr = [1, 2, 3, 4, 5]
for x, y in zip(arr, arr[1:]):
    print(x, y)
