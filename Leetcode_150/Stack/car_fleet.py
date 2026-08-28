# Leetcode Problem 853: Car Fleet

target = 12
positions = [10, 8, 0, 5, 3]
speeds = [2, 4, 1, 1, 3]


def car_fleet(target, positions, speeds):
    """
    Count fleets that arrive at the target without passing each other.

    Parameters:
    target (int): Destination position.
    positions (list): Starting positions.
    speeds (list): Car speeds.

    Returns:
    int: Number of car fleets.
    """
    cars = sorted(zip(positions, speeds), reverse=True)
    times = [(target - position) / speed for position, speed in cars]
    fleets = 0
    slowest = 0
    for time in times:
        if time > slowest:
            fleets += 1
            slowest = time
    return fleets


if __name__ == "__main__":
    result = car_fleet(target, positions, speeds)
    print(f"Car fleets: {result}")