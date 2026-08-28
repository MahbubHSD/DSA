# Leetcode Problem 289: Game of Life

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]


def game_of_life(board):
    """
    Advance Conway's Game of Life by one generation in place.

    Parameters:
    board (list): A grid containing live 1 and dead 0 cells.

    Returns:
    list: The next generation board.
    """
    rows, columns = len(board), len(board[0])
    changes = []
    for row in range(rows):
        for column in range(columns):
            neighbors = sum(
                0 <= next_row < rows and 0 <= next_column < columns and board[next_row][next_column] == 1
                for next_row in range(row - 1, row + 2)
                for next_column in range(column - 1, column + 2)
                if (next_row, next_column) != (row, column)
            )
            if board[row][column] == 1 and neighbors not in (2, 3):
                changes.append((row, column, 0))
            elif board[row][column] == 0 and neighbors == 3:
                changes.append((row, column, 1))
    for row, column, value in changes:
        board[row][column] = value
    return board


if __name__ == "__main__":
    result = game_of_life(board)
    print(f"Next generation: {result}")