"""
Some general hacks
"""
import heapq

# Print on the same line with space as seperator
val = "Hello World"
print(val, end="")

# given n numbers how many pairs can you generate - nC2 - n(n-1) /2

# Read till end of file
input_str = sys.stdin.read().split()

# Getting the top 'n' smallest or largest
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
top_three_largest = heapq.nlargest(3, marks)
print(top_three_largest)
top_three_smallest = heapq.nsmallest(3, marks)

# Using the all() function in python
samples = [5, 6, 7, 8]
check = all(c for c in samples if c > 5)


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
