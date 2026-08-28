# Leetcode Problem 283: Move Zeroes

arr = [0, 1, 0, 3, 12]


def move_zeroes(arr):
    """
    Move all zeroes to the end while preserving non-zero order.

    Parameters:
    arr (list): An integer array.

    Returns:
    list: The modified array.
    """
    write = 0
    for value in arr:
        if value != 0:
            arr[write] = value
            write += 1
    arr[write:] = [0] * (len(arr) - write)
    return arr


if __name__ == "__main__":
    result = move_zeroes(arr)
    print(f"Zeroes moved: {result}")