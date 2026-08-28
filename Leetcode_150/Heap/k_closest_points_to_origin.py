# Leetcode Problem 973: K Closest Points to Origin

points = [[1, 3], [-2, 2], [5, 8]]
k = 2


def k_closest(points, k):
    """
    Return the k points closest to the origin.

    Parameters:
    points (list): Points represented as [x, y].
    k (int): Number of points to return.

    Returns:
    list: The k closest points in any order.
    """
    return sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)[:k]


if __name__ == "__main__":
    result = k_closest(points, k)
    print(f"Closest points: {result}")