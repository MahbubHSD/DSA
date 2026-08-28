# Leetcode Problem 41: First Missing Positive

arr = [3, 4, -1, 1]


def first_missing_positive(arr):
    """
    Find the smallest missing positive integer in an unsorted array.

    Parameters:
    arr (list): An unsorted integer array.

    Returns:
    int: The smallest missing positive value.
    """
    for index in range(len(arr)):
        while 1 <= arr[index] <= len(arr) and arr[arr[index] - 1] != arr[index]:
            target = arr[index] - 1
            arr[index], arr[target] = arr[target], arr[index]
    for index, value in enumerate(arr, 1):
        if value != index:
            return index
    return len(arr) + 1


if __name__ == "__main__":
    result = first_missing_positive(arr)
    print(f"First missing positive: {result}")# Leetcode Problem 41: First Missing Positive

arr = [3, 4, -1, 1]


def first_missing_positive(arr):
    """
    Find the smallest missing positive integer in an unsorted array.

    Parameters:
    arr (list): An unsorted integer array.

    Returns:
    int: The smallest missing positive value.
    """
    for index in range(len(arr)):
        while 1 <= arr[index] <= len(arr) and arr[arr[index] - 1] != arr[index]:
            target = arr[index] - 1
            arr[index], arr[target] = arr[target], arr[index]
    for index, value in enumerate(arr, 1):
        if value != index:
            return index
    return len(arr) + 1


if __name__ == "__main__":
    result = first_missing_positive(arr)
    print(f"First missing positive: {result}")