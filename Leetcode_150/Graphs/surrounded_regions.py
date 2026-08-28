# Leetcode Problem 130: Surrounded Regions

board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]


def capture_surrounded_regions(board):
    """
    Capture O regions that are fully surrounded by X cells.

    Parameters:
    board (list): A board containing X and O cells.

    Returns:
    list: The modified board.
    """
    if not board or not board[0]:
        return board
    rows, columns = len(board), len(board[0])
    stack = [(row, column) for row in range(rows) for column in range(columns) if (row in (0, rows - 1) or column in (0, columns - 1)) and board[row][column] == "O"]
    while stack:
        row, column = stack.pop()
        if not (0 <= row < rows and 0 <= column < columns) or board[row][column] != "O":
            continue
        board[row][column] = "E"
        stack.extend(((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)))
    for row in range(rows):
        for column in range(columns):
            board[row][column] = "O" if board[row][column] == "E" else "X"
    return board


if __name__ == "__main__":
    result = capture_surrounded_regions(board)
    print(f"Captured board: {result}")