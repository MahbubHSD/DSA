# Leetcode Problem 242: Valid Anagram

first_word = "anagram"
second_word = "nagaram"


def is_anagram(first_word, second_word):
    """
    Determine whether two strings are anagrams of each other.

    Parameters:
    first_word (str): The first string.
    second_word (str): The second string.

    Returns:
    bool: True when both strings contain the same characters and frequencies.
    """
    return sorted(first_word) == sorted(second_word)


if __name__ == "__main__":
    result = is_anagram(first_word, second_word)
    print(f"Strings are anagrams: {result}")