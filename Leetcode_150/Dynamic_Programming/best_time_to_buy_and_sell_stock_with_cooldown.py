# Leetcode Problem 309: Best Time to Buy and Sell Stock with Cooldown

prices = [1, 2, 3, 0, 2]


def max_profit_with_cooldown(prices):
    """
    Find maximum stock profit with a one-day cooldown after selling.

    Parameters:
    prices (list): Daily stock prices.

    Returns:
    int: Maximum possible profit.
    """
    held = float("-inf")
    sold = 0
    resting = 0
    for price in prices:
        previous_held, previous_sold = held, sold
        held = max(held, resting - price)
        sold = previous_held + price
        resting = max(resting, previous_sold)
    return max(sold, resting)


if __name__ == "__main__":
    result = max_profit_with_cooldown(prices)
    print(f"Maximum profit with cooldown: {result}")