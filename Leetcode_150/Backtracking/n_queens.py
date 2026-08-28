# Leetcode Problem 51: N-Queens

n = 4


def solve_n_queens(n):
    """
    Place n queens on an n by n board without attacks.

    Parameters:
    n (int): Board dimension.

    Returns:
    list: Board layouts represented by strings.
    """
    result = []
    board = [["."] * n for _ in range(n)]
    columns, diagonals, reverse_diagonals = set(), set(), set()

    def search(row):
        if row == n:
            result.append(["".join(values) for values in board])
            return
        for column in range(n):
            if column in columns or row - column in diagonals or row + column in reverse_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            reverse_diagonals.add(row + column)
            board[row][column] = "Q"
            search(row + 1)
            board[row][column] = "."
            columns.remove(column)
            diagonals.remove(row - column)
            reverse_diagonals.remove(row + column)

    search(0)
    return result


if __name__ == "__main__":
    result = solve_n_queens(n)
    print(f"N-Queens solutions: {len(result)}")