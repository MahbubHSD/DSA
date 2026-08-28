# Leetcode Problem 50: Pow(x, n)

x = 2.0
n = 10


def power(x, n):
    """
    Compute x raised to the integer power n.

    Parameters:
    x (float): The base value.
    n (int): The integer exponent.

    Returns:
    float: x to the power n.
    """
    exponent = n if n >= 0 else -n
    result = 1.0
    while exponent:
        if exponent % 2:
            result *= x
        x *= x
        exponent //= 2
    return result if n >= 0 else 1 / result


if __name__ == "__main__":
    result = power(x, n)
    print(f"Power result: {result}")