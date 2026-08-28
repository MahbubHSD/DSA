# Leetcode Problem 312: Burst Balloons

balloons = [3, 1, 5, 8]


def burst_balloons(balloons):
    """
    Find the maximum coins obtainable by bursting balloons optimally.

    Parameters:
    balloons (list): Positive balloon values.

    Returns:
    int: Maximum coins.
    """
    values = [1] + balloons + [1]
    best = [[0] * len(values) for _ in values]
    for width in range(2, len(values)):
        for left in range(len(values) - width):
            right = left + width
            for middle in range(left + 1, right):
                best[left][right] = max(best[left][right], best[left][middle] + values[left] * values[middle] * values[right] + best[middle][right])
    return best[0][-1]


if __name__ == "__main__":
    result = burst_balloons(balloons)
    print(f"Maximum coins: {result}")