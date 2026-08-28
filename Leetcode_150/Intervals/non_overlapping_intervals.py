# Leetcode Problem 435: Non-overlapping Intervals

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]


def erase_overlap_intervals(intervals):
    """
    Find the minimum intervals to remove for no overlaps.

    Parameters:
    intervals (list): Intervals represented as [start, end].

    Returns:
    int: Minimum number of removals.
    """
    removed = 0
    previous_end = float("-inf")
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if start < previous_end:
            removed += 1
        else:
            previous_end = end
    return removed


if __name__ == "__main__":
    result = erase_overlap_intervals(intervals)
    print(f"Intervals removed: {result}")