# Leetcode Problem 704: Binary Search

arr = [-1, 0, 3, 5, 9, 12]
target = 9


def binary_search(arr, target):
    """
    Find target in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The value to find.

    Returns:
    int: The target index, or -1 when target is absent.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    result = binary_search(arr, target)
    print(f"Target index: {result}")