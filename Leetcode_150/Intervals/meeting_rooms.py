# Leetcode Problem 252: Meeting Rooms

intervals = [[0, 30], [5, 10], [15, 20]]


def can_attend_all_meetings(intervals):
    """
    Determine whether a person can attend every meeting.

    Parameters:
    intervals (list): Meeting intervals as [start, end].

    Returns:
    bool: True when no meetings overlap.
    """
    intervals = sorted(intervals)
    return all(intervals[index][0] >= intervals[index - 1][1] for index in range(1, len(intervals)))


if __name__ == "__main__":
    result = can_attend_all_meetings(intervals)
    print(f"Can attend all meetings: {result}")