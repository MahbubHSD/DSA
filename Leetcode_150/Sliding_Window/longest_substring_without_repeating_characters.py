# Leetcode Problem 3: Longest Substring Without Repeating Characters

text = "abcabcbb"


def length_of_longest_substring(text):
    """
    Find the length of the longest substring without repeated characters.

    Parameters:
    text (str): The string to inspect.

    Returns:
    int: The longest valid substring length.
    """
    last_seen = {}
    left = longest = 0
    for right, character in enumerate(text):
        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1
        last_seen[character] = right
        longest = max(longest, right - left + 1)
    return longest


if __name__ == "__main__":
    result = length_of_longest_substring(text)
    print(f"Longest substring length: {result}")