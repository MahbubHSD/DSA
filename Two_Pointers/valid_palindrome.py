# Leetcode Problem 125: Valid Palindrome

text = "A man, a plan, a canal: Panama"


def is_palindrome(text):
    """
    Determine whether text is a palindrome after removing non-alphanumeric characters.

    Parameters:
    text (str): The text to inspect.

    Returns:
    bool: True if the normalized text is a palindrome.
    """
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    result = is_palindrome(text)
    print(f"Text is a palindrome: {result}")