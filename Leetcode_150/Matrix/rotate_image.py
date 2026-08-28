# Leetcode Problem 48: Rotate Image

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate_image(matrix):
    """
    Rotate an n by n matrix 90 degrees clockwise in place.

    Parameters:
    matrix (list): A square matrix.

    Returns:
    list: The rotated matrix.
    """
    matrix.reverse()
    for row in range(len(matrix)):
        for column in range(row + 1, len(matrix)):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    return matrix


if __name__ == "__main__":
    result = rotate_image(matrix)
    print(f"Rotated matrix: {result}")