# Alternate file for valid_number.py

from valid_number import is_valid_number as _reference_is_valid_number

def is_valid_number(text):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_valid_number(text)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'valid_number.py')
