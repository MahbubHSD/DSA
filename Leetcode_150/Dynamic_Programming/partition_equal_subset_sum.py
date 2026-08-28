# Leetcode Problem 416: Partition Equal Subset Sum

arr = [1, 5, 11, 5]


def can_partition(arr):
    """
    Determine whether values can be divided into two equal-sum subsets.

    Parameters:
    arr (list): Positive integers.

    Returns:
    bool: True when an equal partition exists.
    """
    total = sum(arr)
    if total % 2:
        return False
    possible = {0}
    for value in arr:
        possible |= {current + value for current in possible if current + value <= total // 2}
    return total // 2 in possible


if __name__ == "__main__":
    result = can_partition(arr)
    print(f"Can partition equally: {result}")