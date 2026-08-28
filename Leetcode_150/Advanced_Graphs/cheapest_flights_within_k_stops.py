# Leetcode Problem 787: Cheapest Flights Within K Stops

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]]
source = 0
destination = 3
stops = 1


def cheapest_flight(n, flights, source, destination, stops):
    """
    Find the cheapest route using at most stops intermediate stops.

    Parameters:
    n (int): Number of cities.
    flights (list): Flights represented as [from, to, price].
    source (int): Starting city.
    destination (int): Destination city.
    stops (int): Maximum number of intermediate stops.

    Returns:
    int: Cheapest price, or -1 if no route exists.
    """
    prices = [float("inf")] * n
    prices[source] = 0
    for _ in range(stops + 1):
        next_prices = prices[:]
        for start, end, price in flights:
            if prices[start] != float("inf"):
                next_prices[end] = min(next_prices[end], prices[start] + price)
        prices = next_prices
    return -1 if prices[destination] == float("inf") else prices[destination]


if __name__ == "__main__":
    result = cheapest_flight(n, flights, source, destination, stops)
    print(f"Cheapest flight: {result}")