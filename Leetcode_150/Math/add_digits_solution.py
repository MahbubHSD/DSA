# Alternate file for add_digits.py

from add_digits import add_digits as _reference_add_digits

def add_digits(number):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_add_digits(number)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'add_digits.py')
