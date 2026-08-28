# Leetcode Problem 322: Coin Change

coins = [1, 2, 5]
amount = 11


def coin_change(coins, amount):
    """
    Find the fewest coins needed to make an amount.

    Parameters:
    coins (list): Available coin denominations.
    amount (int): The target amount.

    Returns:
    int: Minimum coin count, or -1 when the amount cannot be made.
    """
    best = [amount + 1] * (amount + 1)
    best[0] = 0
    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                best[current] = min(best[current], best[current - coin] + 1)
    return -1 if best[amount] > amount else best[amount]


if __name__ == "__main__":
    result = coin_change(coins, amount)
    print(f"Minimum coins: {result}")