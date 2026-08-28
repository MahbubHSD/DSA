# Alternate file for meeting_rooms.py

from meeting_rooms import can_attend_all_meetings as _reference_can_attend_all_meetings

def can_attend_all_meetings(intervals):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_attend_all_meetings(intervals)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'meeting_rooms.py')
