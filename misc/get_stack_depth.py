import inspect


def stack_depth():
    """
    Quick function to get the stack depth
    Returns:
    """
    return len(inspect.getouterframes(inspect.currentframe())) - 1
