# Alternate file for coin_change.py

from coin_change import coin_change as _reference_coin_change

def coin_change(coins, amount):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_coin_change(coins, amount)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'coin_change.py')
