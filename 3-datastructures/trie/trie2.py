class PrefixTree:
    """
    This class implements the Trie DataStructure also called as PrefixTree
    """

    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.is_word = False

    def insert(self, word):
        """
        @brief: Function to insert word into Trie data structure
        :param: word - word in the dictionary
        """
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = PrefixTree(letter)
            return self.children[letter].insert(word)
        else:
            self.is_word = True
            return

    def find_children(self, letter):
        """
        @brief: Function to return children of a given letter
        """
        if letter not in self.children:
            return None
        return self.children[letter]
