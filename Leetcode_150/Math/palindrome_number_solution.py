# Alternate file for palindrome_number.py

from palindrome_number import is_palindrome_number as _reference_is_palindrome_number

def is_palindrome_number(number):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_palindrome_number(number)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'palindrome_number.py')
