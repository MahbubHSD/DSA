# Leetcode Problem 49: Group Anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(words):
    """
    Group words that are anagrams of one another.

    Parameters:
    words (list): A list of lowercase words.

    Returns:
    list: Groups of anagram words.
    """
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(words)
    print(f"Anagram groups: {result}")