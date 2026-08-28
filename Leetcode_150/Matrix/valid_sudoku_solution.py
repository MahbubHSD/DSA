# Alternate file for valid_sudoku.py

from valid_sudoku import is_valid_sudoku as _reference_is_valid_sudoku

def is_valid_sudoku(board):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_valid_sudoku(board)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'valid_sudoku.py')
