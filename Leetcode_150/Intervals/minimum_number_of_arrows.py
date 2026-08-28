# Leetcode Problem 452: Minimum Number of Arrows to Burst Balloons

points = [[10, 16], [2, 8], [1, 6], [7, 12]]


def minimum_arrows(points):
    """
    Find the minimum arrows needed to burst all intervals.

    Parameters:
    points (list): Balloon ranges represented as [start, end].

    Returns:
    int: Minimum number of arrows.
    """
    if not points:
        return 0
    arrows = 1
    endpoint = min(end for _, end in points)
    for start, end in sorted(points, key=lambda point: point[0]):
        if start > endpoint:
            arrows += 1
            endpoint = end
        else:
            endpoint = min(endpoint, end)
    return arrows


if __name__ == "__main__":
    result = minimum_arrows(points)
    print(f"Minimum arrows: {result}")