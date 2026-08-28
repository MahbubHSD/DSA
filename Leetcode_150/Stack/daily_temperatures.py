# Leetcode Problem 739: Daily Temperatures

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


def daily_temperatures(temperatures):
    """
    Find how many days until a warmer temperature for each day.

    Parameters:
    temperatures (list): Daily temperatures.

    Returns:
    list: Wait lengths for each day.
    """
    result = [0] * len(temperatures)
    stack = []
    for index, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous = stack.pop()
            result[previous] = index - previous
        stack.append(index)
    return result


if __name__ == "__main__":
    result = daily_temperatures(temperatures)
    print(f"Temperature waits: {result}")