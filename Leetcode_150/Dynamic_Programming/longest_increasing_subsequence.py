# Leetcode Problem 300: Longest Increasing Subsequence

arr = [10, 9, 2, 5, 3, 7, 101, 18]


def longest_increasing_subsequence(arr):
    """
    Find the length of the longest strictly increasing subsequence.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The longest increasing subsequence length.
    """
    lengths = []
    for value in arr:
        left, right = 0, len(lengths)
        while left < right:
            middle = (left + right) // 2
            if lengths[middle] < value:
                left = middle + 1
            else:
                right = middle
        if left == len(lengths):
            lengths.append(value)
        else:
            lengths[left] = value
    return len(lengths)


if __name__ == "__main__":
    result = longest_increasing_subsequence(arr)
    print(f"Longest increasing subsequence length: {result}")