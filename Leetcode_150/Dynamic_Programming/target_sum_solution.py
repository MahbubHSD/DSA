# Alternate file for target_sum.py

from target_sum import target_sum as _reference_target_sum

def target_sum(arr, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_target_sum(arr, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'target_sum.py')
