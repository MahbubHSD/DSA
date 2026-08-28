# Alternate file for two_sum.py

from two_sum import two_sum as _reference_two_sum

def two_sum(arr, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_two_sum(arr, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'two_sum.py')
