"""
Difference Array - When we want to add a value b/w L & R and display the array
"""
A = [5, 4, 1, 2, 3]
print(A)
n = len(A)

# Creating a difference array
diff = [0] * (n+2)
print(diff)

for i in range(n):
    if i == 0:
        diff[i] = A[i]
    else:
        diff[i] = A[i] - A[i-1]

print("The difference aray is:")
print(diff)


# Now let's say I want to add "X" on all elements between index L & R
"""
for i in range(L, R+1):
    A[i] += X
"""

"""
Let's assume there is only 1 query
Let's assume L = 1 and R = 3
"""
L = 1
R = 3
X = 5

diff[L] += X
diff[R+1] -= X

print("The updated difference array is:")
print(diff)

"""
Finally update the the original array based on diff
"""
for i in range(n):
    if i == 0:
        A[i] = diff[i]
    else:
        A[i] = diff[i] + A[i-1]

print("The updated array after querying is:")
print(A)
