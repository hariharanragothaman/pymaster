# DP Problem1 Example

from misc.get_stack_depth import stack_depth


def fibonacci_bruteforce(n):
    """
    O(2**n) time complexity
    Args:
        n:
    Returns:
    """
    print("{indent} fibonacci({n}) called".format(indent=" " * stack_depth(), n=n))
    if n <= 2:
        return 1
    return fibonacci_bruteforce(n-1) + fibonacci_bruteforce(n-2)


def fibonacci_top_down_1(n):
    """
    Args:
        n:
    Returns:
    """
    if n <= 2:
        return 1
    # Setting the cache variable that is 'attached' to this function
    if not hasattr(fibonacci_top_down_1, 'cache'):
        fibonacci_top_down_1.cache = {}


# Now this top-down function can be re-written like this to keep the original function simple
def cached(f):
    cache = {}
    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return worker


@cached
def fibonacci_top_down_2(n):
    if n <= 2:
        return 1
    return fibonacci_top_down_2(n-1) + fibonacci_top_down_2(n-2)


# Now all this can be completely simplified and written as following
# using lru_cache

from functools import lru_cache

# lru_cache by default size is 128
@lru_cache(maxsize=None)
def fibonacci_top_down_3(n):
    if n <= 2:
        return 1
    return fibonacci_top_down_3(n-1) + fibonacci_top_down_3(n-2)


if __name__ == '__main__':
    fibonacci_bruteforce(6)