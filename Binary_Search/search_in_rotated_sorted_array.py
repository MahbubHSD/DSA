# Leetcode Problem 33: Search in Rotated Sorted Array

arr = [4, 5, 6, 7, 0, 1, 2]
target = 0


def search_rotated(arr, target):
    """
    Find target in a rotated sorted array with distinct values.

    Parameters:
    arr (list): A rotated sorted list of integers.
    target (int): The value to find.

    Returns:
    int: The target index, or -1 when target is absent.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        if arr[left] <= arr[middle]:
            if arr[left] <= target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif arr[middle] < target <= arr[right]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    result = search_rotated(arr, target)
    print(f"Target index: {result}")