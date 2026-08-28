# Alternate file for binary_search.py

from binary_search import binary_search as _reference_binary_search

def binary_search(arr, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_binary_search(arr, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'binary_search.py')
