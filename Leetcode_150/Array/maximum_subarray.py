# Leetcode Problem 53: Maximum Subarray

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maximum_subarray(arr):
    """
    Find the largest sum of any contiguous subarray.

    Parameters:
    arr (list): A non-empty list of integers.

    Returns:
    int: The maximum contiguous subarray sum.
    """
    current_sum = best_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    result = maximum_subarray(arr)
    print(f"Maximum subarray sum: {result}")