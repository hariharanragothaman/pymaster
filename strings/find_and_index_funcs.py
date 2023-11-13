a = "abcdabcabcdef"
target = "b"


"""
Using the find() functions for finding index
Returns a '-1' if its not able to find
"""
# regular find:
a.find(target)

# Find b/w 2 indices - returns the lowest index
a.find(target, 2, len(a))

# returns the highest index
a.rfind(target, 0, len(a))

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
