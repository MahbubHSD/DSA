# Leetcode Problem 91: Decode Ways

text = "226"


def decode_ways(text):
    """
    Count ways to decode a digit string as letters 1 through 26.

    Parameters:
    text (str): A string of digits.

    Returns:
    int: Number of valid decodings.
    """
    if not text or text[0] == "0":
        return 0
    previous, current = 1, 1
    for index in range(1, len(text)):
        next_value = (current if text[index] != "0" else 0)
        if 10 <= int(text[index - 1:index + 1]) <= 26:
            next_value += previous
        previous, current = current, next_value
    return current


if __name__ == "__main__":
    result = decode_ways(text)
    print(f"Decode ways: {result}")