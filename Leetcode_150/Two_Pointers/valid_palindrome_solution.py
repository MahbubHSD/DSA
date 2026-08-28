# Alternate file for valid_palindrome.py

from valid_palindrome import is_palindrome as _reference_is_palindrome

def is_palindrome(text):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_palindrome(text)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'valid_palindrome.py')
