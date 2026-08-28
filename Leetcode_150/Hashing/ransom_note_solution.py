# Alternate file for ransom_note.py

from ransom_note import can_construct as _reference_can_construct

def can_construct(ransom, magazine):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_construct(ransom, magazine)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'ransom_note.py')
