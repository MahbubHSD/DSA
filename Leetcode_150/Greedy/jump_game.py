# Leetcode Problem 55: Jump Game

arr = [2, 3, 1, 1, 4]


def can_jump(arr):
    """
    Determine whether the last array index is reachable.

    Parameters:
    arr (list): Maximum jump length at each index.

    Returns:
    bool: True when the last index is reachable.
    """
    furthest = 0
    for index, jump in enumerate(arr):
        if index > furthest:
            return False
        furthest = max(furthest, index + jump)
    return True


if __name__ == "__main__":
    result = can_jump(arr)
    print(f"Can reach the end: {result}")