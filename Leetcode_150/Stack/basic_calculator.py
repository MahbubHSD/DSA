# Leetcode Problem 224: Basic Calculator

expression = "1 + (2 - 3)"


def calculate(expression):
    """
    Evaluate a non-negative integer expression with plus, minus, and parentheses.

    Parameters:
    expression (str): Arithmetic expression.

    Returns:
    int: The expression result.
    """
    result = number = 0
    sign = 1
    stack = []
    for character in expression + "+":
        if character.isdigit():
            number = number * 10 + int(character)
        elif character in "+-":
            result += sign * number
            number = 0
            sign = 1 if character == "+" else -1
        elif character == "(":
            stack.extend((result, sign))
            result, sign = 0, 1
        elif character == ")":
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()
            sign = 1
    return result


if __name__ == "__main__":
    result = calculate(expression)
    print(f"Calculator result: {result}")