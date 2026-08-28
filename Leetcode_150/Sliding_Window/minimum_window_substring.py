# Leetcode Problem 76: Minimum Window Substring

text = "ADOBECODEBANC"
target = "ABC"


def minimum_window(text, target):
    """
    Find the shortest substring containing every target character.

    Parameters:
    text (str): The source string.
    target (str): Required characters and frequencies.

    Returns:
    str: The shortest containing window, or an empty string.
    """
    from collections import Counter

    required = Counter(target)
    window = Counter()
    formed = left = 0
    best = (float("inf"), 0, 0)
    for right, character in enumerate(text):
        window[character] += 1
        if window[character] == required[character]:
            formed += 1
        while formed == len(required):
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            window[text[left]] -= 1
            if window[text[left]] < required[text[left]]:
                formed -= 1
            left += 1
    return text[best[1]:best[2]]


if __name__ == "__main__":
    result = minimum_window(text, target)
    print(f"Minimum window: {result}")