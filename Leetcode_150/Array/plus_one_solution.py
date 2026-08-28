# Alternate file for plus_one.py

from plus_one import plus_one as _reference_plus_one

def plus_one(digits):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_plus_one(digits)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'plus_one.py')
