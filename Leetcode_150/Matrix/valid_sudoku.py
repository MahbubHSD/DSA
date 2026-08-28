# Leetcode Problem 36: Valid Sudoku

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
]


def is_valid_sudoku(board):
    """
    Determine whether filled Sudoku cells obey row, column, and box rules.

    Parameters:
    board (list): A 9 by 9 Sudoku board.

    Returns:
    bool: True when no value is repeated in a unit.
    """
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value == ".":
                continue
            box = (row // 3) * 3 + column // 3
            if value in rows[row] or value in columns[column] or value in boxes[box]:
                return False
            rows[row].add(value)
            columns[column].add(value)
            boxes[box].add(value)
    return True


if __name__ == "__main__":
    result = is_valid_sudoku(board)
    print(f"Sudoku is valid: {result}")