# Flatten a list of lists - Approach 1
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in list1 for item in sublist]
print("The flattened list is:", flat_list)

# Flatten a list of lists - Approach 2
import itertools

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flt = list(itertools.chain.from_iterable(list1))
print("The flattened list is:", flt)
