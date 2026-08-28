# Leetcode Problem 9: Palindrome Number

number = 121


def is_palindrome_number(number):
    """
    Determine whether an integer reads the same in both directions.

    Parameters:
    number (int): The integer to inspect.

    Returns:
    bool: True when number is a palindrome.
    """
    return number >= 0 and str(number) == str(number)[::-1]


if __name__ == "__main__":
    result = is_palindrome_number(number)
    print(f"Number is a palindrome: {result}")