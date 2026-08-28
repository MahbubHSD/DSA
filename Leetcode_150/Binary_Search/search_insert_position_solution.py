# Alternate file for search_insert_position.py

from search_insert_position import search_insert as _reference_search_insert

def search_insert(arr, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_search_insert(arr, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'search_insert_position.py')
