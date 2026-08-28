# Leetcode Problem 26: Remove Duplicates from Sorted Array

arr = [1, 1, 2]


def remove_duplicates(arr):
    """
    Remove duplicates in place from a sorted array.

    Parameters:
    arr (list): A sorted integer array.

    Returns:
    int: Number of unique values left at the beginning of arr.
    """
    if not arr:
        return 0
    write = 1
    for value in arr[1:]:
        if value != arr[write - 1]:
            arr[write] = value
            write += 1
    return write


if __name__ == "__main__":
    length = remove_duplicates(arr)
    print(f"Unique values: {arr[:length]}")