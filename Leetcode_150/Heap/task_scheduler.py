# Leetcode Problem 621: Task Scheduler

tasks = ["A", "A", "A", "B", "B", "B"]
cooldown = 2


def least_interval(tasks, cooldown):
    """
    Find the shortest schedule honoring the cooldown between equal tasks.

    Parameters:
    tasks (list): Task labels.
    cooldown (int): Required idle intervals between equal labels.

    Returns:
    int: Minimum schedule length.
    """
    from collections import Counter

    frequencies = sorted(Counter(tasks).values(), reverse=True)
    frame = (frequencies[0] - 1) * (cooldown + 1)
    frame += sum(frequency == frequencies[0] for frequency in frequencies)
    return max(len(tasks), frame)


if __name__ == "__main__":
    result = least_interval(tasks, cooldown)
    print(f"Least schedule length: {result}")