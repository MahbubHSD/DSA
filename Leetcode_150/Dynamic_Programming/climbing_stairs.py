# Leetcode Problem 70: Climbing Stairs

n = 5


def climbing_stairs(n):
    """
    Count ways to reach the nth stair using one- or two-step moves.

    Parameters:
    n (int): The number of stairs.

    Returns:
    int: The number of distinct ways.
    """
    previous, current = 1, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


if __name__ == "__main__":
    result = climbing_stairs(n)
    print(f"Ways to climb stairs: {result}")