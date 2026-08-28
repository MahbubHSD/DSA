# Leetcode Problem 162: Find Peak Element

arr = [1, 2, 3, 1]


def find_peak(arr):
    """
    Find an index whose value is greater than its neighbors.

    Parameters:
    arr (list): Adjacent values are distinct.

    Returns:
    int: Index of any peak element.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] > arr[middle + 1]:
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == "__main__":
    result = find_peak(arr)
    print(f"Peak index: {result}")