# Leetcode Problem 217: Contains Duplicate

arr = [1, 2, 3, 1]


def contains_duplicate(arr):
    """
    Determine whether the array contains any duplicate values.

    Parameters:
    arr (list): A list of values.

    Returns:
    bool: True if a value appears more than once; otherwise, False.
    """
    return len(arr) != len(set(arr))


if __name__ == "__main__":
    result = contains_duplicate(arr)
    print(f"Array contains a duplicate: {result}")