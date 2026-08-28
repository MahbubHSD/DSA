# Leetcode Problem 377: Combination Sum IV

numbers = [1, 2, 3]
target = 4


def combination_sum_count(numbers, target):
    """
    Count ordered combinations that add up to target.

    Parameters:
    numbers (list): Positive available numbers.
    target (int): Required sum.

    Returns:
    int: Number of ordered combinations.
    """
    ways = [0] * (target + 1)
    ways[0] = 1
    for current in range(1, target + 1):
        ways[current] = sum(ways[current - number] for number in numbers if number <= current)
    return ways[target]


if __name__ == "__main__":
    result = combination_sum_count(numbers, target)
    print(f"Combination count: {result}")