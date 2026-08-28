# Leetcode Problem 253: Meeting Rooms II

intervals = [[0, 30], [5, 10], [15, 20]]


def minimum_meeting_rooms(intervals):
    """
    Find the minimum rooms needed for all meetings.

    Parameters:
    intervals (list): Meeting intervals as [start, end].

    Returns:
    int: Minimum number of rooms required.
    """
    events = sorted((time, 1 if kind == "start" else -1) for start, end in intervals for time, kind in ((start, "start"), (end, "end")))
    rooms = best = 0
    for _, change in events:
        rooms += change
        best = max(best, rooms)
    return best


if __name__ == "__main__":
    result = minimum_meeting_rooms(intervals)
    print(f"Meeting rooms needed: {result}")