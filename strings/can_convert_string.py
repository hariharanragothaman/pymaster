# Setdefault feature example
# String transforms to another string problem?
def can_convert(s1, s2):
    """ Convert 2 strings of same length by doing zero or more conversions"""
    if s1 == s2:
        return True
    dp = {}
    for i, j in zip(s1, s2):
        if dp.setdefault(i, j) != j:
            return False
    return len(set(s2)) < 26
