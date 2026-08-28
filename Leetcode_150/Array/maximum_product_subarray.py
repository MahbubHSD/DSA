# Leetcode Problem 152: Maximum Product Subarray

arr = [2, 3, -2, 4]


def maximum_product_subarray(arr):
    """
    Find the largest product of a contiguous subarray.

    Parameters:
    arr (list): A non-empty list of integers.

    Returns:
    int: The maximum contiguous product.
    """
    current_max = current_min = result = arr[0]
    for value in arr[1:]:
        candidates = (value, value * current_max, value * current_min)
        current_max = max(candidates)
        current_min = min(candidates)
        result = max(result, current_max)
    return result


if __name__ == "__main__":
    result = maximum_product_subarray(arr)
    print(f"Maximum product: {result}")