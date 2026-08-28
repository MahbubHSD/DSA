# Leetcode Problem 45: Jump Game II

arr = [2, 3, 1, 1, 4]


def minimum_jumps(arr):
    """
    Find the minimum jumps needed to reach the final index.

    Parameters:
    arr (list): Maximum jump distance at each index.

    Returns:
    int: Minimum jump count.
    """
    jumps = current_end = furthest = 0
    for index in range(len(arr) - 1):
        furthest = max(furthest, index + arr[index])
        if index == current_end:
            jumps += 1
            current_end = furthest
    return jumps


if __name__ == "__main__":
    result = minimum_jumps(arr)
    print(f"Minimum jumps: {result}")