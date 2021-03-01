"""
Fenwick Tree and it's applications

Let f(x) be some reversible function and A be an array of integers of length N

Fenwick tree is a datastructure that has the following properties
    a. Calculates the value of the function f in the given range [l,r] - in O(logn) time.
    b. updates the value of an element of A in O(logn) time.
    c. requires O(N) memory, exactly requires the same memory as of A
    d. is easy to use and code in 2D arrays

Fenwwick tree is also called as - Binary Indexed Tree or BIT
Note - Here f(x) can be any function - for quick understanding we can have it as a sum() function
"""


class FenwickTree:
    def __init__(self, x):
        """ Transform list into Binary Indexed Tree"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]
