# Leetcode Problem 97: Interleaving String

first = "aabcc"
second = "dbbca"
target = "aadbbcbcac"


def is_interleaving(first, second, target):
    """
    Determine whether target interleaves two strings in order.

    Parameters:
    first (str): First source string.
    second (str): Second source string.
    target (str): Candidate interleaved string.

    Returns:
    bool: True when target is a valid interleaving.
    """
    if len(first) + len(second) != len(target):
        return False
    possible = [False] * (len(second) + 1)
    possible[0] = True
    for second_index in range(1, len(second) + 1):
        possible[second_index] = possible[second_index - 1] and second[second_index - 1] == target[second_index - 1]
    for first_index in range(1, len(first) + 1):
        possible[0] = possible[0] and first[first_index - 1] == target[first_index - 1]
        for second_index in range(1, len(second) + 1):
            possible[second_index] = (possible[second_index] and first[first_index - 1] == target[first_index + second_index - 1]) or (possible[second_index - 1] and second[second_index - 1] == target[first_index + second_index - 1])
    return possible[-1]


if __name__ == "__main__":
    result = is_interleaving(first, second, target)
    print(f"Valid interleaving: {result}")