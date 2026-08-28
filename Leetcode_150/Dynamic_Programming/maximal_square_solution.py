# Alternate file for maximal_square.py

from maximal_square import maximal_square as _reference_maximal_square

def maximal_square(matrix):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_maximal_square(matrix)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'maximal_square.py')
