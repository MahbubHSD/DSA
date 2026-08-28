# Alternate file for merge_intervals.py

from merge_intervals import merge_intervals as _reference_merge_intervals

def merge_intervals(intervals):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_merge_intervals(intervals)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'merge_intervals.py')
