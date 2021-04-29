# Longest Common Substring - given 2 strings
from difflib import SequenceMatcher


def find_length(A, B):
    if set(A).isdisjoint(B):
        return 0
    a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(
        0, len(A), 0, len(B)
    )
    return size
