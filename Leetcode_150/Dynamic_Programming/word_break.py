# Leetcode Problem 139: Word Break

text = "leetcode"
dictionary = ["leet", "code"]


def word_break(text, dictionary):
    """
    Determine whether text can be split into dictionary words.

    Parameters:
    text (str): The string to split.
    dictionary (list): Allowed words.

    Returns:
    bool: True when a complete split exists.
    """
    words = set(dictionary)
    possible = [False] * (len(text) + 1)
    possible[0] = True
    for end in range(1, len(text) + 1):
        possible[end] = any(possible[start] and text[start:end] in words for start in range(end))
    return possible[-1]


if __name__ == "__main__":
    result = word_break(text, dictionary)
    print(f"Can split text: {result}")