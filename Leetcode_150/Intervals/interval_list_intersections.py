# Leetcode Problem 986: Interval List Intersections

first = [[0, 2], [5, 10], [13, 23], [24, 25]]
second = [[1, 5], [8, 12], [15, 24], [25, 26]]


def interval_intersections(first, second):
    """Return intersections of two sorted, disjoint interval lists."""
    result = []
    left = right = 0
    while left < len(first) and right < len(second):
        start = max(first[left][0], second[right][0])
        end = min(first[left][1], second[right][1])
        if start <= end:
            result.append([start, end])
        if first[left][1] < second[right][1]:
            left += 1
        else:
            right += 1
    return result


if __name__ == "__main__":
    print(f"Intersections: {interval_intersections(first, second)}")