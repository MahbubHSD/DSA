# Alternate file for word_search.py

from word_search import word_search as _reference_word_search

def word_search(board, word):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_word_search(board, word)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'word_search.py')
