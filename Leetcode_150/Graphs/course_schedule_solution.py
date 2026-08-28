# Alternate file for course_schedule.py

from course_schedule import can_finish as _reference_can_finish

def can_finish(number_of_courses, prerequisites):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_finish(number_of_courses, prerequisites)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'course_schedule.py')
