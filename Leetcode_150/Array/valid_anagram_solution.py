# Alternate file for valid_anagram.py

from valid_anagram import is_anagram as _reference_is_anagram

def is_anagram(first_word, second_word):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_is_anagram(first_word, second_word)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'valid_anagram.py')
