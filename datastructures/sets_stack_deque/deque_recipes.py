from collections import deque

q = deque()
q.append(5)  # Adds value to the right
q.append(234)
q.append(576)

count = q.count(5)  # Returns the count of value
q.extend([10])  # Extends takes only an iterable as argument
q.extendleft([15])  # Extends to the left
q.insert(1, 7)  # Inserts value at given index

removed_element = q.pop()  # Returns an element from right-size of the queue
left_pop = q.popleft()  # Pops from left-side used in BFS

# deque also supports functions such as len(), reverse(), sum() etc & is subscriptable
# Famous deque recipes are 'tail' and 'moving-average'
"""
# Bounded length queues can provide functionality of tail filter in Unix
"""


def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)


# Another approach to using deque is to maintain a sequence of recently added elements
# By appending to the right and popping from the left - Transforms into fixed sliding window
