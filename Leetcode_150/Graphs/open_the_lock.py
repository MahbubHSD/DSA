# Leetcode Problem 752: Open the Lock

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"


def open_lock(deadends, target):
    """
    Find the fewest turns needed to reach a lock target.

    Parameters:
    deadends (list): Combinations that cannot be entered.
    target (str): Desired four-wheel combination.

    Returns:
    int: Minimum turns, or -1 when unreachable.
    """
    from collections import deque

    blocked = set(deadends)
    if "0000" in blocked:
        return -1
    queue = deque([("0000", 0)])
    seen = {"0000"}
    while queue:
        state, turns = queue.popleft()
        if state == target:
            return turns
        for index in range(4):
            digit = int(state[index])
            for change in (-1, 1):
                next_digit = (digit + change) % 10
                next_state = state[:index] + str(next_digit) + state[index + 1:]
                if next_state not in blocked and next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, turns + 1))
    return -1


if __name__ == "__main__":
    result = open_lock(deadends, target)
    print(f"Minimum lock turns: {result}")