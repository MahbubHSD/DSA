# Alternate file for open_the_lock.py

from open_the_lock import open_lock as _reference_open_lock

def open_lock(deadends, target):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_open_lock(deadends, target)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'open_the_lock.py')
