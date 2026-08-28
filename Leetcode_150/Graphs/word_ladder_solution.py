# Alternate file for word_ladder.py

from word_ladder import word_ladder as _reference_word_ladder

def word_ladder(begin_word, end_word, word_list):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_word_ladder(begin_word, end_word, word_list)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'word_ladder.py')
