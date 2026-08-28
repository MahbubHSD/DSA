# Leetcode Problem 494: Target Sum

arr = [1, 1, 1, 1, 1]
target = 3


def target_sum(arr, target):
    """
    Count ways to assign plus or minus signs to reach target.

    Parameters:
    arr (list): Non-negative integers.
    target (int): Required signed sum.

    Returns:
    int: Number of valid sign assignments.
    """
    ways = {0: 1}
    for value in arr:
        next_ways = {}
        for total, count in ways.items():
            next_ways[total + value] = next_ways.get(total + value, 0) + count
            next_ways[total - value] = next_ways.get(total - value, 0) + count
        ways = next_ways
    return ways.get(target, 0)


if __name__ == "__main__":
    result = target_sum(arr, target)
    print(f"Target sum ways: {result}")