# Leetcode Problem 88: Merge Sorted Array


def merge_sorted_array(first, first_size, second, second_size):
    """
    Merge two sorted arrays into the first array in place.

    Parameters:
    first (list): First sorted array with trailing space.
    first_size (int): Number of valid values in first.
    second (list): Second sorted array.
    second_size (int): Number of valid values in second.

    Returns:
    list: The merged sorted array.
    """
    first_index, second_index, write_index = first_size - 1, second_size - 1, first_size + second_size - 1
    while second_index >= 0:
        if first_index >= 0 and first[first_index] > second[second_index]:
            first[write_index] = first[first_index]
            first_index -= 1
        else:
            first[write_index] = second[second_index]
            second_index -= 1
        write_index -= 1
    return first


if __name__ == "__main__":
    result = merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(f"Merged array: {result}")