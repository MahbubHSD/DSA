# Leetcode Problem 57: Insert Interval

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]


def insert_interval(intervals, new_interval):
    """
    Insert an interval and merge any resulting overlaps.

    Parameters:
    intervals (list): Sorted, non-overlapping intervals.
    new_interval (list): The interval to insert.

    Returns:
    list: Sorted, non-overlapping intervals after insertion.
    """
    result = []
    index = 0
    while index < len(intervals) and intervals[index][1] < new_interval[0]:
        result.append(intervals[index])
        index += 1
    while index < len(intervals) and intervals[index][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[index][0])
        new_interval[1] = max(new_interval[1], intervals[index][1])
        index += 1
    result.append(new_interval)
    return result + intervals[index:]


if __name__ == "__main__":
    result = insert_interval(intervals, new_interval)
    print(f"Intervals after insertion: {result}")