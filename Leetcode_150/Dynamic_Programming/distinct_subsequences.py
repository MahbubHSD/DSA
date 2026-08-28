# Leetcode Problem 115: Distinct Subsequences

source = "rabbbit"
target = "rabbit"


def distinct_subsequences(source, target):
    """
    Count distinct ways target can be formed as a source subsequence.

    Parameters:
    source (str): The source string.
    target (str): The target subsequence.

    Returns:
    int: Number of distinct subsequences.
    """
    ways = [0] * (len(target) + 1)
    ways[0] = 1
    for source_character in source:
        for index in range(len(target), 0, -1):
            if source_character == target[index - 1]:
                ways[index] += ways[index - 1]
    return ways[-1]


if __name__ == "__main__":
    result = distinct_subsequences(source, target)
    print(f"Distinct subsequences: {result}")