# Leetcode Problem 931: Minimum Falling Path Sum

matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]


def minimum_falling_path_sum(matrix):
    """Find the smallest sum of a top-to-bottom falling path."""
    totals = matrix[0][:]
    for row in matrix[1:]:
        totals = [value + min(totals[max(0, column - 1):column + 2]) for column, value in enumerate(row)]
    return min(totals)


if __name__ == "__main__":
    print(f"Minimum falling path: {minimum_falling_path_sum(matrix)}")