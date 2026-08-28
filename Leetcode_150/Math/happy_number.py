# Leetcode Problem 202: Happy Number

n = 19


def is_happy(n):
    """
    Determine whether repeated digit-square sums reach one.

    Parameters:
    n (int): A positive integer.

    Returns:
    bool: True when n is a happy number.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


if __name__ == "__main__":
    result = is_happy(n)
    print(f"Number is happy: {result}")