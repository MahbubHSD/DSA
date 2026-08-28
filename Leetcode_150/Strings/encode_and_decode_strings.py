# Leetcode Problem 271: Encode and Decode Strings

words = ["lint", "code", "love", "you"]


def encode(words):
    """
    Encode a list of strings into one unambiguous string.

    Parameters:
    words (list): Strings to encode.

    Returns:
    str: The encoded representation.
    """
    return "".join(f"{len(word)}#{word}" for word in words)


def decode(text):
    """
    Decode text produced by encode.

    Parameters:
    text (str): An encoded string.

    Returns:
    list: The original strings.
    """
    words = []
    index = 0
    while index < len(text):
        separator = text.index("#", index)
        length = int(text[index:separator])
        start = separator + 1
        words.append(text[start:start + length])
        index = start + length
    return words


if __name__ == "__main__":
    result = decode(encode(words))
    print(f"Decoded words: {result}")