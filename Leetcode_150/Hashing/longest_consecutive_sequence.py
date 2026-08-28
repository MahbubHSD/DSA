# Leetcode Problem 128: Longest Consecutive Sequence

arr = [100, 4, 200, 1, 3, 2]


def longest_consecutive(arr):
    """
    Find the length of the longest consecutive integer sequence.

    Parameters:
    arr (list): An unsorted list of integers.

    Returns:
    int: The length of the longest consecutive sequence.
    """
    values = set(arr)
    longest = 0
    for value in values:
        if value - 1 not in values:
            length = 1
            while value + length in values:
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == "__main__":
    result = longest_consecutive(arr)
    print(f"Longest consecutive sequence: {result}")