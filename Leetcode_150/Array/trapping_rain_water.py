# Leetcode Problem 42: Trapping Rain Water

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap_rain_water(heights):
    """
    Calculate water trapped between elevation bars.

    Parameters:
    heights (list): Non-negative bar heights.

    Returns:
    int: Total trapped water.
    """
    left, right = 0, len(heights) - 1
    left_max = right_max = water = 0
    while left < right:
        if heights[left] <= heights[right]:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    return water


if __name__ == "__main__":
    result = trap_rain_water(heights)
    print(f"Trapped rain water: {result}")