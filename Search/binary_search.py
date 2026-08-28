def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Perform binary search on a sorted array to find the index of the target value using recursion.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.
    left (int): The left index of the current search range.
    right (int): The right index of the current search range.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # Target was not found

    mid = left + (right - left) // 2

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If target is greater, ignore left half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # If target is smaller, ignore right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)