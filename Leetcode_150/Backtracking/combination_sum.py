# Leetcode Problem 39: Combination Sum

candidates = [2, 3, 6, 7]
target = 7


def combination_sum(candidates, target):
    """
    Find combinations that add to target; values may be reused.

    Parameters:
    candidates (list): Positive candidate values.
    target (int): The required sum.

    Returns:
    list: Unique combinations adding to target.
    """
    result = []

    def search(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        for index in range(start, len(candidates)):
            value = candidates[index]
            if value > remaining:
                continue
            current.append(value)
            search(index, remaining - value, current)
            current.pop()

    search(0, target, [])
    return result


if __name__ == "__main__":
    result = combination_sum(candidates, target)
    print(f"Combinations: {result}")