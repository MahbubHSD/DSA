# Leetcode Problem 424: Longest Repeating Character Replacement

text = "AABABBA"
k = 1


def character_replacement(text, k):
    """
    Find the longest substring after at most k character replacements.

    Parameters:
    text (str): An uppercase string.
    k (int): Maximum replacements.

    Returns:
    int: Longest possible uniform substring length.
    """
    from collections import Counter

    counts = Counter()
    left = max_count = result = 0
    for right, character in enumerate(text):
        counts[character] += 1
        max_count = max(max_count, counts[character])
        while right - left + 1 - max_count > k:
            counts[text[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    result = character_replacement(text, k)
    print(f"Longest replacement window: {result}")