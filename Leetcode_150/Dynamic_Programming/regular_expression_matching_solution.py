# Alternate file for regular_expression_matching.py

from regular_expression_matching import regex_match as _reference_regex_match

def regex_match(text, pattern):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_regex_match(text, pattern)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'regular_expression_matching.py')
