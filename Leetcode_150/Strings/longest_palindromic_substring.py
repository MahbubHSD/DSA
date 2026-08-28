# Leetcode Problem 5: Longest Palindromic Substring

text = "babad"


def longest_palindromic_substring(text):
    """
    Find the longest palindromic substring.

    Parameters:
    text (str): The string to inspect.

    Returns:
    str: A longest palindromic substring.
    """
    best = ""
    for index in range(len(text)):
        for left, right in ((index, index), (index, index + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                if right - left + 1 > len(best):
                    best = text[left:right + 1]
                left -= 1
                right += 1
    return best


if __name__ == "__main__":
    result = longest_palindromic_substring(text)
    print(f"Longest palindromic substring: {result}")