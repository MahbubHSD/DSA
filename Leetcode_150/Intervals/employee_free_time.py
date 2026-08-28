# Leetcode Problem 759: Employee Free Time

schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]


def employee_free_time(schedule):
    """
    Find intervals when every employee is free.

    Parameters:
    schedule (list): Each employee's sorted busy intervals.

    Returns:
    list: Shared free intervals.
    """
    intervals = sorted(interval for employee in schedule for interval in employee)
    result = []
    current_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start > current_end:
            result.append([current_end, start])
        current_end = max(current_end, end)
    return result


if __name__ == "__main__":
    result = employee_free_time(schedule)
    print(f"Shared free time: {result}")