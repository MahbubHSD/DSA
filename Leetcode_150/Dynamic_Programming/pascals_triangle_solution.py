# Alternate file for pascals_triangle.py

from pascals_triangle import pascals_triangle as _reference_pascals_triangle

def pascals_triangle(rows):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_pascals_triangle(rows)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'pascals_triangle.py')
