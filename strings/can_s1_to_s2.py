"""
Given two strings str1 and str2 of the same length
Determine whether you can transform str1 into str2 by doing zero or more conversions.
In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.
Return true if and only if you can transform str1 into str2.
"""

def can_convert(s1, s2) -> bool:
    """Convert 2 strings of same length by doing zero or more conversions"""
    if s1 == s2:
        return True
    dp = {}
    for i, j in zip(s1, s2):
        if dp.setdefault(i, j) != j:
            return False
    return len(set(s2)) < 26
