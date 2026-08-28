# Leetcode Problem 188: Best Time to Buy and Sell Stock IV

prices = [3, 2, 6, 5, 0, 3]
k = 2


def max_profit_k_transactions(k, prices):
    """
    Find maximum profit using at most k stock transactions.

    Parameters:
    k (int): Maximum transaction count.
    prices (list): Daily stock prices.

    Returns:
    int: Maximum possible profit.
    """
    if not prices or k == 0:
        return 0
    if k >= len(prices) // 2:
        return sum(max(0, prices[index] - prices[index - 1]) for index in range(1, len(prices)))
    profits = [0] * (k + 1)
    holds = [float("-inf")] * (k + 1)
    for price in prices:
        for transaction in range(1, k + 1):
            holds[transaction] = max(holds[transaction], profits[transaction - 1] - price)
            profits[transaction] = max(profits[transaction], holds[transaction] + price)
    return profits[k]


if __name__ == "__main__":
    result = max_profit_k_transactions(k, prices)
    print(f"Maximum profit: {result}")