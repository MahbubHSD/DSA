# Leetcode Problem 11: Container With Most Water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area(heights):
    """
    Find the greatest area formed by two vertical lines.

    Parameters:
    heights (list): Heights of vertical lines.

    Returns:
    int: Maximum container area.
    """
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    result = max_area(heights)
    print(f"Maximum container area: {result}")