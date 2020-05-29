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

# deque also supports functions such as len(), reverse(), sum() etc
# Famous deque recipes are 'tail' and 'moving-average'
