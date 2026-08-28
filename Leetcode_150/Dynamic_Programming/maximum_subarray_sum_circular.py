# Leetcode Problem 918: Maximum Sum Circular Subarray

arr = [1, -2, 3, -2]


def maximum_circular_sum(arr):
    """
    Find the maximum sum of a non-empty circular subarray.

    Parameters:
    arr (list): A non-empty integer array.

    Returns:
    int: Maximum circular subarray sum.
    """
    total = sum(arr)
    current_max = best_max = arr[0]
    current_min = best_min = arr[0]
    for value in arr[1:]:
        current_max = max(value, current_max + value)
        best_max = max(best_max, current_max)
        current_min = min(value, current_min + value)
        best_min = min(best_min, current_min)
    return best_max if best_max < 0 else max(best_max, total - best_min)


if __name__ == "__main__":
    result = maximum_circular_sum(arr)
    print(f"Maximum circular sum: {result}")