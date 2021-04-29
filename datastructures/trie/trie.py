class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        # Check if word exists:
        current_dict = self.root

        if self.__contains__(word):
            for letter in word:
                current_dict = current_dict[letter]
            current_dict["_cnt_"] += 1
            return

        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True
        current_dict["_cnt_"] = 1

    def __contains__(self, word):
        """
        Check for the _end_ flag
        """
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        """
        Removes the boolean for _end_
        """
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]

    def starts_with(self, prefix):
        current_dict = self.root
        for letter in prefix:
            current = current_dict.get(letter)
            if current is None:
                return False
            current_dict = current_dict[letter]
        return True

    def count_words_equal_to(self, word: str) -> int:
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return 0
            current_dict = current_dict[letter]
        return current_dict["_cnt_"]


if __name__ == "__main__":
    words = ["hello", "world", "wow", "delete", "dell", "hello"]
    t = Trie(*words)
    print("Printing the trie", t.root)

    # Checking for basic contains
    res = t.__contains__("world")
    print(res)

    # Checking for prefix
    res = t.starts_with("worl")
    print(res)

    # Checking for basic contains before deletion
    res = t.__contains__("delete")
    print(res)

    # Checking for contains after deletion
    t.__delitem__("delete")
    res = t.__contains__("delete")
    print(res)
    print(t.root)

    val = t.count_words_equal_to("hello")
    print("The count is:", val)
