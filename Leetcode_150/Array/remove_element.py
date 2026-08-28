# Leetcode Problem 27: Remove Element

arr = [3, 2, 2, 3]
value = 3


def remove_element(arr, value):
    """Remove value in place and return the remaining length."""
    write = 0
    for current in arr:
        if current != value:
            arr[write] = current
            write += 1
    return write


if __name__ == "__main__":
    length = remove_element(arr, value)
    print(f"Remaining values: {arr[:length]}")