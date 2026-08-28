# Leetcode Problem 347: Top K Frequent Elements

arr = [1, 1, 1, 2, 2, 3]
k = 2


def top_k_frequent(arr, k):
    """
    Return the k values with the highest frequencies.

    Parameters:
    arr (list): A list of values.
    k (int): Number of frequent values to return.

    Returns:
    list: The k most frequent values.
    """
    from collections import Counter

    return [value for value, _ in Counter(arr).most_common(k)]


if __name__ == "__main__":
    result = top_k_frequent(arr, k)
    print(f"Top frequent values: {result}")