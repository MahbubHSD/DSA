# Leetcode Problem 647: Palindromic Substrings

text = "aaa"


def count_palindromic_substrings(text):
    """
    Count every palindromic substring in text.

    Parameters:
    text (str): The string to inspect.

    Returns:
    int: Number of palindromic substrings.
    """
    count = 0
    for center in range(len(text)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                count += 1
                left -= 1
                right += 1
    return count


if __name__ == "__main__":
    result = count_palindromic_substrings(text)
    print(f"Palindromic substrings: {result}")