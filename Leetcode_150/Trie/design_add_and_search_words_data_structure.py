# Leetcode Problem 211: Design Add and Search Words Data Structure


class WordDictionary:
    """Store words and search them with '.' wildcard characters."""

    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)

    def search(self, word):
        return any(
            len(candidate) == len(word)
            and all(
                expected == actual or expected == "."
                for expected, actual in zip(word, candidate)
            )
            for candidate in self.words
        )


if __name__ == "__main__":
    dictionary = WordDictionary()
    dictionary.add_word("bad")
    print(f"Wildcard search: {dictionary.search('.ad')}")