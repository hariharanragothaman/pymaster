"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
"""



class Solution:
    def rotatedDigits(self, N: int) -> int:
        k = 1
        cnt = 0
        while k <= N:
            s = str(k)
            # These if rotated give invalid
            if all(d not in '347' for d in s):
                # These digits rotate and give valid
                if any(d in '2569' for d in s):
                    cnt += 1
            k += 1
        return cnt