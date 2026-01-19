a = "abcdabcabcdef"
target = "b"


"""
Using the find() functions for finding index
Returns a '-1' if its not able to find
Use find instead of index, mostly.
"""
# regular find:
def find_first_index(a, target):
    idx = a.find(target)
    return idx

def find_between_two_indexes(a, target, low, high):
    idx = a.find(target, low, high)
    return idx

# returns the highest index
def find_highest_index(a, target):
    idx = a.rfind(target, 0, len(a))
    return idx

"""
Using the index() function
This raises a ValueError if it's not found
always returns the lowest index
"""
res = a.index(target)
op = a.index(target, 2, 7)

# Similar to rfind - there is rindex - but raises a ValueError
# This returns the highest index
op = a.rindex(target, 2, 7)


if __name__ == '__main__':
    a = "abcdabcabcdef"
    target = "b"
    find_first_index(a, target)
    low, high = 2, 7
    find_between_two_indexes(a, target, low, high)
    find_highest_index(a, target)
