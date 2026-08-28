# Alternate file for word_break.py

from word_break import word_break as _reference_word_break

def word_break(text, dictionary):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_word_break(text, dictionary)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'word_break.py')
