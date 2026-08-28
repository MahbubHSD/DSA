# Leetcode Problem 65: Valid Number

text = "2e10"


def is_valid_number(text):
    """
    Determine whether text represents a valid decimal number.

    Parameters:
    text (str): Candidate number text.

    Returns:
    bool: True when text follows decimal and exponent rules.
    """
    try:
        value = float(text)
    except ValueError:
        return False
    return value not in (float("inf"), float("-inf")) and "nan" not in text.lower()


if __name__ == "__main__":
    result = is_valid_number(text)
    print(f"Valid number: {result}")