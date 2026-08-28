# Leetcode Problem 56: Merge Intervals

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge_intervals(intervals):
    """
    Merge all overlapping intervals.

    Parameters:
    intervals (list): Intervals represented as [start, end].

    Returns:
    list: Non-overlapping merged intervals.
    """
    merged = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


if __name__ == "__main__":
    result = merge_intervals(intervals)
    print(f"Merged intervals: {result}")