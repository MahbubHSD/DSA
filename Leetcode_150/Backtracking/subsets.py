# Leetcode Problem 78: Subsets

arr = [1, 2, 3]


def subsets(arr):
    """
    Generate every subset of an array of unique values.

    Parameters:
    arr (list): A list of unique values.

    Returns:
    list: All possible subsets.
    """
    result = [[]]
    for value in arr:
        result += [subset + [value] for subset in result]
    return result


if __name__ == "__main__":
    result = subsets(arr)
    print(f"Subsets: {result}")