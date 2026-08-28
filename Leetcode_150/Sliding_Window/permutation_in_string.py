# Leetcode Problem 567: Permutation in String

first = "ab"
second = "eidbaooo"


def contains_permutation(first, second):
    """
    Determine whether second contains a permutation of first.

    Parameters:
    first (str): Pattern string.
    second (str): String to search.

    Returns:
    bool: True when a matching character window exists.
    """
    from collections import Counter

    required = Counter(first)
    window = Counter(second[:len(first)])
    if window == required:
        return True
    for index in range(len(first), len(second)):
        window[second[index]] += 1
        outgoing = second[index - len(first)]
        window[outgoing] -= 1
        if window[outgoing] == 0:
            del window[outgoing]
        if window == required:
            return True
    return False


if __name__ == "__main__":
    result = contains_permutation(first, second)
    print(f"Contains permutation: {result}")