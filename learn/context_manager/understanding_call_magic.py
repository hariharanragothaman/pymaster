class FooBar:
    def __init__(self, sample_string):
        self.s = sample_string

    def __call__(self, *args, **kwargs):
        """Since this takes arguments, we can pass whatever we want into this"""
        print("Entering the call object")


if __name__ == "__main__":
    f = FooBar("example")
    # So the instance is allowed to behave a function
    f()
