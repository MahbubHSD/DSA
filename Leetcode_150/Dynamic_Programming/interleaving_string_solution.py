# Alternate file for interleaving_string.py

from interleaving_string import is_interleaving as _reference_is_interleaving

def is_interleaving(first, second, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_interleaving(first, second, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'interleaving_string.py')
