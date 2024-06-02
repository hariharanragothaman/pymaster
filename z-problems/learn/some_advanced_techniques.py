from functools import partial

# dict is a constructor - class dict(**kwarg)

hmap = dict(a=1, b=2, c=3)
print(hmap)


def send_info(**kwargs):
    for key, value in kwargs.items():
        print(f"parameter name: {key}; value: {value}")


send_info(text="HelloWorld", age="infinity")

# Using Partial() - Basics
def greeting(word, person):
    print(f"{word}, {person}")


greeting("Hello", "Chammu")

custom_greet = partial(greeting, "Hi")
custom_greet("World")
