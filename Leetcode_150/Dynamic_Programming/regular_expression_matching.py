# Leetcode Problem 10: Regular Expression Matching

text = "aab"
pattern = "c*a*b"


def regex_match(text, pattern):
    """
    Match text against a pattern supporting '.' and '*'.

    Parameters:
    text (str): Text to match.
    pattern (str): Pattern with '.' and '*' operators.

    Returns:
    bool: True when the complete text matches the pattern.
    """
    possible = [False] * (len(pattern) + 1)
    possible[0] = True
    for index in range(2, len(pattern) + 1):
        if pattern[index - 1] == "*":
            possible[index] = possible[index - 2]
    for text_index in range(1, len(text) + 1):
        previous = possible[:]
        possible[0] = False
        for pattern_index in range(1, len(pattern) + 1):
            token = pattern[pattern_index - 1]
            if token == "." or token == text[text_index - 1]:
                possible[pattern_index] = previous[pattern_index - 1]
            elif token == "*":
                preceding = pattern[pattern_index - 2]
                possible[pattern_index] = possible[pattern_index - 2] or ((preceding == "." or preceding == text[text_index - 1]) and previous[pattern_index])
            else:
                possible[pattern_index] = False
    return possible[-1]


if __name__ == "__main__":
    result = regex_match(text, pattern)
    print(f"Pattern matches: {result}")