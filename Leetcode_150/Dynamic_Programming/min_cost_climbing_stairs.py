# Leetcode Problem 746: Min Cost Climbing Stairs

cost = [10, 15, 20]


def min_cost_climbing_stairs(cost):
    """
    Find the minimum cost to reach the top of a staircase.

    Parameters:
    cost (list): Cost of stepping on each stair.

    Returns:
    int: Minimum cost to move beyond the final stair.
    """
    previous = current = 0
    for value in cost:
        previous, current = current, value + min(previous, current)
    return min(previous, current)


if __name__ == "__main__":
    result = min_cost_climbing_stairs(cost)
    print(f"Minimum climbing cost: {result}")