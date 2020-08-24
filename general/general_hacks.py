import heapq

# Print on the same line with space as seperator
val = "Hello World"
print(val, end="")

# Getting the top 'n' smallest or largest
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
top_three_largest = heapq.nlargest(3, marks)
print(top_three_largest)
top_three_smallest = heapq.nsmallest(3, marks)

# Using the all() function in python
samples = [5, 6, 7, 8]
check = all(c for c in samples if c > 5)

# Flatten a list of lists
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in list1 for item in sublist]

# Let's say we have 2 tuples - we need to convert it into a hashmap
t1 = (1, 2, 3)
t2 = (4, 5, 6)
mapping = dict(zip(t1, t2))

# Basic example of Lambda
addition = lambda x, y : x + y
addition(4, 5)

# Writing if - else in one-line
y = 20
x = 5 if y > 10 else 25

str = "Hello"
if "le" in str:
    print("Awesome")

a = True and 6.2
print(a)