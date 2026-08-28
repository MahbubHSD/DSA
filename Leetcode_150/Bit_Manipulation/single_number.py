# Leetcode Problem 136: Single Number

arr = [4, 1, 2, 1, 2]


def single_number(arr):
    """
    Find the value that occurs once when every other value occurs twice.

    Parameters:
    arr (list): Integers with exactly one unpaired value.

    Returns:
    int: The unpaired value.
    """
    result = 0
    for value in arr:
        result ^= value
    return result


if __name__ == "__main__":
    result = single_number(arr)
    print(f"Single number: {result}")