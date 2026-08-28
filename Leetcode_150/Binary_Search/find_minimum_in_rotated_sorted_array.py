# Leetcode Problem 153: Find Minimum in Rotated Sorted Array

arr = [3, 4, 5, 1, 2]


def find_minimum(arr):
    """
    Find the minimum value in a rotated sorted array.

    Parameters:
    arr (list): A rotated sorted array with distinct values.

    Returns:
    int: The minimum value.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle
    return arr[left]


if __name__ == "__main__":
    result = find_minimum(arr)
    print(f"Minimum value: {result}")