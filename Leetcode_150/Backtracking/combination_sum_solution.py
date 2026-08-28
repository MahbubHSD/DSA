# Alternate file for combination_sum.py

from combination_sum import combination_sum as _reference_combination_sum

def combination_sum(candidates, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_combination_sum(candidates, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'combination_sum.py')
