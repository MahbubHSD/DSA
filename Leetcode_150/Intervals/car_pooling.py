# Leetcode Problem 1094: Car Pooling

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4


def can_carpool(trips, capacity):
    """
    Determine whether all passengers can fit during a route.

    Parameters:
    trips (list): Trips represented as [passengers, start, end].
    capacity (int): Vehicle capacity.

    Returns:
    bool: True when capacity is never exceeded.
    """
    changes = {}
    for passengers, start, end in trips:
        changes[start] = changes.get(start, 0) + passengers
        changes[end] = changes.get(end, 0) - passengers
    onboard = 0
    for location in sorted(changes):
        onboard += changes[location]
        if onboard > capacity:
            return False
    return True


if __name__ == "__main__":
    result = can_carpool(trips, capacity)
    print(f"Can carpool: {result}")