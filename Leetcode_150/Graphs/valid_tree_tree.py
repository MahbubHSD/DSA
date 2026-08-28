# Alternate file for valid_tree.py

from valid_tree import valid_tree as _reference_valid_tree

def valid_tree(n, edges):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_valid_tree(n, edges)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'valid_tree.py')
