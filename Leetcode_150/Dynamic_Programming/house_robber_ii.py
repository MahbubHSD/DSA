# Leetcode Problem 213: House Robber II

money = [2, 3, 2]


def circular_house_robber(money):
    """
    Maximize robbery from circularly arranged non-adjacent houses.

    Parameters:
    money (list): Money at each circular house.

    Returns:
    int: Maximum amount that can be robbed.
    """
    if len(money) == 1:
        return money[0]

    def rob(values):
        previous = current = 0
        for amount in values:
            previous, current = current, max(current, previous + amount)
        return current

    return max(rob(money[:-1]), rob(money[1:]))


if __name__ == "__main__":
    result = circular_house_robber(money)
    print(f"Maximum circular robbery: {result}")