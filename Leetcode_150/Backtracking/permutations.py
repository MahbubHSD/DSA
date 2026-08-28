# Leetcode Problem 46: Permutations

arr = [1, 2, 3]


def permutations(arr):
    """
    Generate all permutations of distinct values.

    Parameters:
    arr (list): Distinct values to arrange.

    Returns:
    list: Every possible ordering.
    """
    result = []

    def search(remaining, current):
        if not remaining:
            result.append(current[:])
            return
        for index, value in enumerate(remaining):
            search(remaining[:index] + remaining[index + 1:], current + [value])

    search(arr, [])
    return result


if __name__ == "__main__":
    result = permutations(arr)
    print(f"Permutations: {result}")