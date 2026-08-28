# Leetcode Problem 228: Summary Ranges

arr = [0, 1, 2, 4, 5, 7]


def summary_ranges(arr):
    """
    Summarize consecutive runs in a sorted unique array.

    Parameters:
    arr (list): Sorted unique integers.

    Returns:
    list: Range strings covering every value.
    """
    result = []
    start = 0
    for index in range(1, len(arr) + 1):
        if index == len(arr) or arr[index] != arr[index - 1] + 1:
            end = arr[index - 1]
            result.append(str(arr[start]) if start == index - 1 else f"{arr[start]}->{end}")
            start = index
    return result


if __name__ == "__main__":
    result = summary_ranges(arr)
    print(f"Summary ranges: {result}")