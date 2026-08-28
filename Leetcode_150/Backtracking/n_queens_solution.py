# Alternate file for n_queens.py

from n_queens import solve_n_queens as _reference_solve_n_queens

def solve_n_queens(n):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_solve_n_queens(n)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'n_queens.py')
