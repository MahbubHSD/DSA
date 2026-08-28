# Leetcode Problem 215: Kth Largest Element in an Array

arr = [3, 2, 1, 5, 6, 4]
k = 2


def find_kth_largest(arr, k):
    """
    Find the kth largest value in an unsorted array.

    Parameters:
    arr (list): A list of integers.
    k (int): The one-based rank from largest to smallest.

    Returns:
    int: The kth largest value.
    """
    import heapq

    return heapq.nlargest(k, arr)[-1]


if __name__ == "__main__":
    result = find_kth_largest(arr, k)
    print(f"Kth largest value: {result}")