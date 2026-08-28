# Leetcode Problem 198: House Robber

money = [2, 7, 9, 3, 1]


def house_robber(money):
    """
    Find the maximum money that can be robbed without adjacent houses.

    Parameters:
    money (list): Money available at each house.

    Returns:
    int: The maximum amount that can be robbed.
    """
    two_houses_back = one_house_back = 0
    for amount in money:
        two_houses_back, one_house_back = one_house_back, max(
            one_house_back, two_houses_back + amount
        )
    return one_house_back


if __name__ == "__main__":
    result = house_robber(money)
    print(f"Maximum robbed amount: {result}")