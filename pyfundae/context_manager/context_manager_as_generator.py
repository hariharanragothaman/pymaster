from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        # Line #7 == __enter__
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with open_file("../misc/test.txt", "r") as f:
    print(f.read())
