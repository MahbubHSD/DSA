# Leetcode Problem 208: Implement Trie (Prefix Tree)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """Prefix tree supporting insertion and prefix lookup."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for character in word:
            node = node.children.setdefault(character, TrieNode())
        node.is_word = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, text):
        node = self.root
        for character in text:
            if character not in node.children:
                return None
            node = node.children[character]
        return node


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(f"Search apple: {trie.search('apple')}")
    print(f"Prefix app: {trie.starts_with('app')}")