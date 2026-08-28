# Leetcode Problem 64: Minimum Path Sum

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]


def minimum_path_sum(grid):
    """
    Find the minimum top-left to bottom-right grid path sum.

    Parameters:
    grid (list): A non-negative integer grid.

    Returns:
    int: Minimum path sum using right and down moves.
    """
    totals = [0] * len(grid[0])
    totals[0] = grid[0][0]
    for column in range(1, len(grid[0])):
        totals[column] = totals[column - 1] + grid[0][column]
    for row in range(1, len(grid)):
        totals[0] += grid[row][0]
        for column in range(1, len(grid[0])):
            totals[column] = grid[row][column] + min(totals[column], totals[column - 1])
    return totals[-1]


if __name__ == "__main__":
    result = minimum_path_sum(grid)
    print(f"Minimum path sum: {result}")