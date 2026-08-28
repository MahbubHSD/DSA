# Leetcode Problem 150: Evaluate Reverse Polish Notation

tokens = ["2", "1", "+", "3", "*"]


def evaluate_rpn(tokens):
    """
    Evaluate an arithmetic expression written in reverse Polish notation.

    Parameters:
    tokens (list): Numbers and operators in postfix order.

    Returns:
    int: The expression result, truncated toward zero for division.
    """
    stack = []
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
            continue
        right = stack.pop()
        left = stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            stack.append(int(left / right))
    return stack[-1]


if __name__ == "__main__":
    result = evaluate_rpn(tokens)
    print(f"RPN result: {result}")