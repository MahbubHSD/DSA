# Leetcode Problem 54: Spiral Matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def spiral_order(matrix):
    """
    Return matrix values in clockwise spiral order.

    Parameters:
    matrix (list): A rectangular matrix.

    Returns:
    list: Matrix values in spiral order.
    """
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1] if matrix else []
        matrix = [list(row) for row in matrix]
    return result


if __name__ == "__main__":
    result = spiral_order(matrix)
    print(f"Spiral order: {result}")