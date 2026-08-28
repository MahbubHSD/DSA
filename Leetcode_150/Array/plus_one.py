# Leetcode Problem 66: Plus One

digits = [1, 2, 9]


def plus_one(digits):
    """Add one to a number represented by a digit list."""
    for index in range(len(digits) - 1, -1, -1):
        if digits[index] < 9:
            digits[index] += 1
            return digits
        digits[index] = 0
    return [1] + digits


if __name__ == "__main__":
    print(f"After adding one: {plus_one(digits)}")