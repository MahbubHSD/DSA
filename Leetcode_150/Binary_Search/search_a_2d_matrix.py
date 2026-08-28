# Leetcode Problem 74: Search a 2D Matrix

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3


def search_matrix(matrix, target):
    """
    Search for a value in a row-sorted matrix.

    Parameters:
    matrix (list): Rows sorted and ordered by row.
    target (int): Value to find.

    Returns:
    bool: True when target occurs in the matrix.
    """
    if not matrix or not matrix[0]:
        return False
    columns = len(matrix[0])
    left, right = 0, len(matrix) * columns - 1
    while left <= right:
        middle = (left + right) // 2
        value = matrix[middle // columns][middle % columns]
        if value == target:
            return True
        if value < target:
            left = middle + 1
        else:
            right = middle - 1
    return False


if __name__ == "__main__":
    result = search_matrix(matrix, target)
    print(f"Target found: {result}")