"""
Functionality between local vs global
"""

# Case 1: nolocal is used when we need to access a variable in a nested function


def func1():
    x = 5

    def func2():
        nonlocal x
        print(x)

    func2()


func1()

# More common problematic scenario - where we think it's global but it's not.
x = 5


def func3():
    # Add this line, actually makes it reference the globally declared x
    global x
    x += 5


func3()
