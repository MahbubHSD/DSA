# Alternate file for task_scheduler.py

from task_scheduler import least_interval as _reference_least_interval

def least_interval(tasks, cooldown):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_least_interval(tasks, cooldown)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'task_scheduler.py')
