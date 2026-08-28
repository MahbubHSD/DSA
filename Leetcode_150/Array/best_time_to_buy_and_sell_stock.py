# Leetcode Problem 121: Best Time to Buy and Sell Stock

prices = [7, 1, 5, 3, 6, 4]


def max_profit(prices):
    """
    Find the maximum profit from one buy and one later sell.

    Parameters:
    prices (list): Daily stock prices.

    Returns:
    int: The maximum possible profit.
    """
    lowest_price = float("inf")
    best_profit = 0

    for price in prices:
        lowest_price = min(lowest_price, price)
        best_profit = max(best_profit, price - lowest_price)

    return best_profit


if __name__ == "__main__":
    result = max_profit(prices)
    print(f"Maximum profit: {result}")