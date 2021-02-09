import time

def logging_time(func):
    """ Decorator that logs the time """
    def logger():
        start = time.time()
        func()
        print(f"Calling {func.__name__} : {time.time() - start:.5f}")
    
    return logger

@logging_time
def calculate_sum():
    return sum(range(100000))

calculate_sum()