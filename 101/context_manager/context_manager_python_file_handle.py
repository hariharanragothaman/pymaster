# To define an Class for Opening a file


class OpenFile:
    def __init__(self, filename, mode):
        print("Entering the constructor")
        self.file_name = filename
        self.mode = mode
        self.file = None
        return

    def __enter__(self):
        print("Calling the __enter__ method")
        self.file_handler = open(self.file_name, self.mode)
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Calling __exit__ method", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return


with OpenFile("../misc/test.txt", "r") as f:
    print("Reading a file")
    print(f.read())
