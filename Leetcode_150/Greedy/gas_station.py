# Leetcode Problem 134: Gas Station

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]


def gas_station(gas, cost):
    """
    Find the starting station for completing a circular route.

    Parameters:
    gas (list): Gas available at each station.
    cost (list): Gas required to reach the next station.

    Returns:
    int: A valid starting index, or -1 when no route exists.
    """
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for index, amount in enumerate(gas):
        tank += amount - cost[index]
        if tank < 0:
            start = index + 1
            tank = 0
    return start


if __name__ == "__main__":
    result = gas_station(gas, cost)
    print(f"Starting station: {result}")