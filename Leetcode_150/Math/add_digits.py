# Leetcode Problem 258: Add Digits

number = 38


def add_digits(number):
    """Repeatedly add digits until one digit remains."""
    return 0 if number == 0 else 1 + (number - 1) % 9


if __name__ == "__main__":
    print(f"Digital root: {add_digits(number)}")