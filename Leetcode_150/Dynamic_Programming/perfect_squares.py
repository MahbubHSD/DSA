# Leetcode Problem 279: Perfect Squares

n = 12


def num_squares(n):
    """
    Find the least number of perfect squares summing to n.

    Parameters:
    n (int): A positive integer.

    Returns:
    int: Minimum number of square values.
    """
    best = [0] + [n + 1] * n
    for value in range(1, n + 1):
        square = 1
        while square * square <= value:
            best[value] = min(best[value], best[value - square * square] + 1)
            square += 1
    return best[n]


if __name__ == "__main__":
    result = num_squares(n)
    print(f"Minimum perfect squares: {result}")