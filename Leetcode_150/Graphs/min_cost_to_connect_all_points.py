# Leetcode Problem 1584: Min Cost to Connect All Points

points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]


def min_cost_connect_points(points):
    """
    Find the minimum Manhattan distance needed to connect all points.

    Parameters:
    points (list): Point coordinates represented as [x, y].

    Returns:
    int: Weight of a minimum spanning tree.
    """
    connected = {0}
    distances = [float("inf")] * len(points)
    total = 0
    while len(connected) < len(points):
        best_point = -1
        best_distance = float("inf")
        for point in connected:
            for candidate in range(len(points)):
                if candidate not in connected:
                    distance = abs(points[point][0] - points[candidate][0]) + abs(points[point][1] - points[candidate][1])
                    if distance < distances[candidate]:
                        distances[candidate] = distance
                    if distances[candidate] < best_distance:
                        best_distance = distances[candidate]
                        best_point = candidate
        connected.add(best_point)
        total += best_distance
    return total


if __name__ == "__main__":
    result = min_cost_connect_points(points)
    print(f"Minimum connection cost: {result}")