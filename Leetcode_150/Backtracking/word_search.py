# Leetcode Problem 79: Word Search

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"


def word_search(board, word):
    """
    Determine whether a word can be traced through adjacent board cells.

    Parameters:
    board (list): A character grid.
    word (str): The word to find.

    Returns:
    bool: True when the word exists without reusing a cell.
    """
    rows, columns = len(board), len(board[0])

    def search(row, column, index):
        if index == len(word):
            return True
        if row < 0 or row >= rows or column < 0 or column >= columns:
            return False
        if board[row][column] != word[index]:
            return False
        value = board[row][column]
        board[row][column] = "#"
        found = any(search(next_row, next_column, index + 1) for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)))
        board[row][column] = value
        return found

    return any(search(row, column, 0) for row in range(rows) for column in range(columns))


if __name__ == "__main__":
    result = word_search(board, word)
    print(f"Word exists: {result}")