# Leetcode Problem 84: Largest Rectangle in Histogram

heights = [2, 1, 5, 6, 2, 3]


def largest_rectangle(heights):
    """
    Find the largest rectangle that fits inside a histogram.

    Parameters:
    heights (list): Histogram bar heights.

    Returns:
    int: Largest rectangle area.
    """
    stack = []
    best = 0
    for index, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            bar = stack.pop()
            left = stack[-1] + 1 if stack else 0
            best = max(best, heights[bar] * (index - left))
        stack.append(index)
    return best


if __name__ == "__main__":
    result = largest_rectangle(heights)
    print(f"Largest rectangle area: {result}")