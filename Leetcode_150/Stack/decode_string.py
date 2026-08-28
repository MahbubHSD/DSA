# Leetcode Problem 394: Decode String

text = "3[a2[c]]"


def decode_string(text):
    """
    Decode nested repetition expressions such as 3[a2[c]].

    Parameters:
    text (str): Encoded string containing counts and brackets.

    Returns:
    str: Decoded string.
    """
    numbers = []
    strings = []
    current = ""
    number = 0
    for character in text:
        if character.isdigit():
            number = number * 10 + int(character)
        elif character == "[":
            numbers.append(number)
            strings.append(current)
            number = 0
            current = ""
        elif character == "]":
            current = strings.pop() + current * numbers.pop()
        else:
            current += character
    return current


if __name__ == "__main__":
    result = decode_string(text)
    print(f"Decoded string: {result}")