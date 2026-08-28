# Leetcode Problem 8: String to Integer (atoi)

text = " -42"


def string_to_integer(text):
    """
    Convert a string to a signed 32-bit integer using atoi rules.

    Parameters:
    text (str): Input text.

    Returns:
    int: Parsed and clamped integer.
    """
    index = 0
    while index < len(text) and text[index] == " ":
        index += 1
    sign = -1 if index < len(text) and text[index] == "-" else 1
    if index < len(text) and text[index] in "+-":
        index += 1
    value = 0
    while index < len(text) and text[index].isdigit():
        value = value * 10 + int(text[index])
        index += 1
    value *= sign
    return max(-(2 ** 31), min(2 ** 31 - 1, value))


if __name__ == "__main__":
    result = string_to_integer(text)
    print(f"Parsed integer: {result}")