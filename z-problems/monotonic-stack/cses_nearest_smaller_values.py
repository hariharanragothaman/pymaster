"""
Given an array of n integers, your task is to find for each array position the nearest position to its left having a smaller value.

Input

The first input line has an integer n: the size of the array.

The second line has n integers x1,x2,…,xn: the array values.

Output

Print n integers: for each array position the nearest position with a smaller value. If there is no such position, print 0.

Constraints
1≤n≤2⋅105
1≤xi≤109
"""


def nearest_smaller_values(A, n):
    for i in range(n):
        candidates = A[:i]
        j = len(candidates) - 1

        """ So this method is not efficient since to find j, we are popping entirely, 
            so if the array is very big - this will TLE easily.
        """
        while candidates and candidates[-1] >= A[i]:
            candidates.pop()
            j -= 1

        if j == -1:
            print(0, end=" ")
        else:
            print(j + 1, end=" ")


def nearest_smaller_values_optimized(A, n):
    """This is maintaining a monotonic stack?"""
    result = ""

    """
    Good optimzations
    1. Here we have the stack created once
    2. Since we care only about index - we store the index in the stack
    3. If we care about the values, we can either go with the index approach, and get the value?
        or we can easily use a deepcopy of the original array
    "The core concept being - the stack itself is sorted - or increasing.
        This creates us a binary search like scenario
    """

    """ Adding zero for one-indexing"""
    stack = [0]
    A = [0] + A

    print("The array is:")
    print(*A)

    for i in range(1, n + 1):
        print("The incoming number is:", A[i])
        while A[stack[-1]] >= A[i]:
            stack.pop()
        result += str(stack[-1]) + " "
        stack.append(i)
        print("The stack is:", stack)
        print("*" * 10)
    print(result)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    nearest_smaller_values_optimized(arr, n)
