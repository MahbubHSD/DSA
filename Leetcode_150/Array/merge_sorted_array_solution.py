# Alternate file for merge_sorted_array.py

from merge_sorted_array import merge_sorted_array as _reference_merge_sorted_array

def merge_sorted_array(first, first_size, second, second_size):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_merge_sorted_array(first, first_size, second, second_size)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'merge_sorted_array.py')
