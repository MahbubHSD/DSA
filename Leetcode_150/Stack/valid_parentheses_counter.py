# Counter-based approach for Valid Parentheses

def is_valid_parentheses_counter(text):
    """
    Keep a simple counter for each bracket type and reject invalid closers.
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    print(is_valid_parentheses_counter('()[]{}'))
    print(is_valid_parentheses_counter('([)]'))
