class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        print("The word is:", word)
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
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

if __name__ == '__main__':
    words = ["hello", "world", "wow"]
    t = Trie(*words)
    print(t.root)
    res = t.__contains__('wow')
    print(res)
    res = t.starts_with('worl')
    print(res)
