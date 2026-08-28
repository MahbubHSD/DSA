# Leetcode Problem 172: Factorial Trailing Zeroes

n = 25


def trailing_zeroes(n):
    """
    Count trailing zeroes in n factorial.

    Parameters:
    n (int): Factorial input.

    Returns:
    int: Number of trailing zeroes in n!.
    """
    result = 0
    while n:
        n //= 5
        result += n
    return result


if __name__ == "__main__":
    result = trailing_zeroes(n)
    print(f"Trailing zeroes: {result}")