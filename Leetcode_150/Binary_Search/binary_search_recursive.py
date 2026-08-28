# Recursive binary search approach

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Return the index of target using recursive binary search.
    If not found, return -1.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    middle = left + (right - left) // 2

    if arr[middle] == target:
        return middle
    if arr[middle] > target:
        return binary_search_recursive(arr, target, left, middle - 1)
    return binary_search_recursive(arr, target, middle + 1, right)


if __name__ == "__main__":
    numbers = [-1, 0, 3, 5, 9, 12]
    print(binary_search_recursive(numbers, 9))
    print(binary_search_recursive(numbers, 4))
