def two_pointer_search(arr, target):
    """
    Perform a two-pointer search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Check if the target is present at left pointer
        if arr[left] == target:
            return left
        # Check if the target is present at right pointer
        elif arr[right] == target:
            return right
        
        # Move pointers towards each other
        left += 1
        right -= 1

    # Target was not found in the array
    return -1