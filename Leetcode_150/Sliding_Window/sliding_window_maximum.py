# Leetcode Problem 239: Sliding Window Maximum

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def max_sliding_window(arr, k):
    """
    Find the maximum value in every window of size k.

    Parameters:
    arr (list): A list of integers.
    k (int): Window size.

    Returns:
    list: Maximum values for each window.
    """
    from collections import deque

    result = []
    window = deque()
    for index, value in enumerate(arr):
        while window and window[0] <= index - k:
            window.popleft()
        while window and arr[window[-1]] <= value:
            window.pop()
        window.append(index)
        if index >= k - 1:
            result.append(arr[window[0]])
    return result


if __name__ == "__main__":
    result = max_sliding_window(arr, k)
    print(f"Window maximums: {result}")