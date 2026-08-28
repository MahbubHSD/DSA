# Alternate file for edit_distance.py

from edit_distance import edit_distance as _reference_edit_distance

def edit_distance(first_word, second_word):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_edit_distance(first_word, second_word)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'edit_distance.py')
