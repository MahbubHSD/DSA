# Alternate file for basic_calculator.py

from basic_calculator import calculate as _reference_calculate

def calculate(expression):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_calculate(expression)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'basic_calculator.py')
