# Leetcode Problem 73: Set Matrix Zeroes

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def set_zeroes(matrix):
    """
    Set an entire row and column to zero when a cell is zero.

    Parameters:
    matrix (list): A rectangular integer matrix.

    Returns:
    list: The modified matrix.
    """
    zero_rows = {row for row, values in enumerate(matrix) if 0 in values}
    zero_columns = {
        column
        for column in range(len(matrix[0]))
        if any(matrix[row][column] == 0 for row in range(len(matrix)))
    }
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row in zero_rows or column in zero_columns:
                matrix[row][column] = 0
    return matrix


if __name__ == "__main__":
    result = set_zeroes(matrix)
    print(f"Matrix after zeroing: {result}")