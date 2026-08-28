# Leetcode Problem 221: Maximal Square

matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]


def maximal_square(matrix):
    """
    Find the area of the largest square containing only ones.

    Parameters:
    matrix (list): A binary matrix represented by strings.

    Returns:
    int: Largest square area.
    """
    if not matrix:
        return 0
    previous = [0] * (len(matrix[0]) + 1)
    best = 0
    for row in matrix:
        current = [0]
        for column, value in enumerate(row, 1):
            if value == "1":
                current.append(1 + min(previous[column], current[-1], previous[column - 1]))
                best = max(best, current[-1])
            else:
                current.append(0)
        previous = current
    return best * best


if __name__ == "__main__":
    result = maximal_square(matrix)
    print(f"Maximal square area: {result}")