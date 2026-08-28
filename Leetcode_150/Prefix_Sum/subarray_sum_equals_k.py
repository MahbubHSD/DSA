# Leetcode Problem 560: Subarray Sum Equals K

arr = [1, 1, 1]
k = 2


def subarray_sum(arr, k):
    """
    Count contiguous subarrays whose sum equals k.

    Parameters:
    arr (list): An integer array.
    k (int): The required sum.

    Returns:
    int: The number of matching subarrays.
    """
    prefix_counts = {0: 1}
    prefix = result = 0
    for value in arr:
        prefix += value
        result += prefix_counts.get(prefix - k, 0)
        prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
    return result


if __name__ == "__main__":
    result = subarray_sum(arr, k)
    print(f"Subarrays with sum {k}: {result}")