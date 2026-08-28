# Alternate file for four_sum.py

from four_sum import four_sum as _reference_four_sum

def four_sum(arr, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_four_sum(arr, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'four_sum.py')
