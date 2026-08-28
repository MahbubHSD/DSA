# Leetcode Problem 994: Rotting Oranges

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]


def rotting_oranges(grid):
    """
    Find minutes required for rot to reach every orange.

    Parameters:
    grid (list): 0 is empty, 1 is fresh, and 2 is rotten.

    Returns:
    int: Minutes required, or -1 if a fresh orange remains.
    """
    from collections import deque

    queue = deque()
    fresh = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 2:
                queue.append((row, column))
            elif grid[row][column] == 1:
                fresh += 1
    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):
            row, column = queue.popleft()
            for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                if 0 <= next_row < len(grid) and 0 <= next_column < len(grid[0]) and grid[next_row][next_column] == 1:
                    grid[next_row][next_column] = 2
                    fresh -= 1
                    queue.append((next_row, next_column))
        minutes += 1
    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    result = rotting_oranges(grid)
    print(f"Minutes to rot oranges: {result}")