# Leetcode Problem 62: Unique Paths

m = 3
n = 7


def unique_paths(m, n):
    """
    Count paths from the top-left to bottom-right of an m by n grid.

    Parameters:
    m (int): Number of rows.
    n (int): Number of columns.

    Returns:
    int: Number of paths using only right and down moves.
    """
    paths = [1] * n
    for _ in range(m - 1):
        for column in range(1, n):
            paths[column] += paths[column - 1]
    return paths[-1]


if __name__ == "__main__":
    result = unique_paths(m, n)
    print(f"Unique paths: {result}")