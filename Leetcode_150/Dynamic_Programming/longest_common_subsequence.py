# Leetcode Problem 1143: Longest Common Subsequence

first_text = "abcde"
second_text = "ace"


def longest_common_subsequence(first_text, second_text):
    """
    Find the length of the longest subsequence shared by two strings.

    Parameters:
    first_text (str): The first string.
    second_text (str): The second string.

    Returns:
    int: The shared subsequence length.
    """
    previous = [0] * (len(second_text) + 1)
    for first_character in first_text:
        current = [0]
        for index, second_character in enumerate(second_text, 1):
            if first_character == second_character:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[-1]))
        previous = current
    return previous[-1]


if __name__ == "__main__":
    result = longest_common_subsequence(first_text, second_text)
    print(f"Longest common subsequence length: {result}")