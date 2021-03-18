"""
    Basic well used example of context_manager
    This file contains a lot of pseudo code, and will not independently run
"""
# opening and closing of a file

fd = open(filename)
try:
    process_file(fd)
finally:
    fd.close()

# Now the above code can be re-written using a with statement

with open(filename) as fd:
    process_file(fd)