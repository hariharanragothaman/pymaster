import time


def logging_time(func):
    """Decorator that logs the time"""

    def logger(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"Calling {func.__name__} : {time.time() - start:.5f}")

    return logger


@logging_time
def calculate_sum():
    """Function to calculate sum"""
    return sum(range(100000))


calculate_sum()
print(calculate_sum.__doc__)
