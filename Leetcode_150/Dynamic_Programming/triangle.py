# Leetcode Problem 120: Triangle

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]


def minimum_triangle_total(triangle):
    """
    Find the minimum top-to-bottom path sum in a triangle.

    Parameters:
    triangle (list): Rows of triangle values.

    Returns:
    int: Minimum path total.
    """
    totals = triangle[-1][:]
    for row in range(len(triangle) - 2, -1, -1):
        for column in range(len(triangle[row])):
            totals[column] = triangle[row][column] + min(totals[column], totals[column + 1])
    return totals[0]


if __name__ == "__main__":
    result = minimum_triangle_total(triangle)
    print(f"Minimum triangle total: {result}")