# Leetcode Problem 75: Sort Colors

arr = [2, 0, 2, 1, 1, 0]


def sort_colors(arr):
    """
    Sort an array containing only 0, 1, and 2 in place.

    Parameters:
    arr (list): An array of color values.

    Returns:
    list: The sorted array.
    """
    low = middle = 0
    high = len(arr) - 1
    while middle <= high:
        if arr[middle] == 0:
            arr[low], arr[middle] = arr[middle], arr[low]
            low += 1
            middle += 1
        elif arr[middle] == 2:
            arr[middle], arr[high] = arr[high], arr[middle]
            high -= 1
        else:
            middle += 1
    return arr


if __name__ == "__main__":
    result = sort_colors(arr)
    print(f"Sorted colors: {result}")