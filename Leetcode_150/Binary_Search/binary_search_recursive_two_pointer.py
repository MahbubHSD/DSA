# Alternate file for binary_search_recursive.py

from binary_search_recursive import binary_search_recursive as _reference_binary_search_recursive

def binary_search_recursive(arr, target, left, right):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_binary_search_recursive(arr, target, left, right)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'binary_search_recursive.py')
