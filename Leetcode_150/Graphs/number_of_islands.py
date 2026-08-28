# Leetcode Problem 200: Number of Islands

grid = [["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]


def number_of_islands(grid):
    """
    Count connected groups of land in a rectangular grid.

    Parameters:
    grid (list): A grid containing "1" for land and "0" for water.

    Returns:
    int: The number of islands.
    """
    rows = len(grid)
    columns = len(grid[0]) if rows else 0
    islands = 0

    def visit(row, column):
        if row < 0 or row >= rows or column < 0 or column >= columns:
            return
        if grid[row][column] != "1":
            return
        grid[row][column] = "0"
        visit(row + 1, column)
        visit(row - 1, column)
        visit(row, column + 1)
        visit(row, column - 1)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "1":
                islands += 1
                visit(row, column)
    return islands


if __name__ == "__main__":
    result = number_of_islands(grid)
    print(f"Number of islands: {result}")