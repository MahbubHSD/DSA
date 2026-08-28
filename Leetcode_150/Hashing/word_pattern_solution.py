# Alternate file for word_pattern.py

from word_pattern import follows_pattern as _reference_follows_pattern

def follows_pattern(pattern, text):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_follows_pattern(pattern, text)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'word_pattern.py')
