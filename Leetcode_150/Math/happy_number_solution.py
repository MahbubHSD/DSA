# Alternate file for happy_number.py

from happy_number import is_happy as _reference_is_happy

def is_happy(n):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_happy(n)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'happy_number.py')
