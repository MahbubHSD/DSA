# Alternate file for interval_list_intersections.py

from interval_list_intersections import interval_intersections as _reference_interval_intersections

def interval_intersections(first, second):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_interval_intersections(first, second)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'interval_list_intersections.py')
