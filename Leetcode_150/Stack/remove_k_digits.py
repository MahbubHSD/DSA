# Leetcode Problem 402: Remove K Digits

number = "1432219"
k = 3


def remove_k_digits(number, k):
    """Remove k digits to create the smallest possible non-negative number."""
    stack = []
    for digit in number:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k:
        stack = stack[:-k]
    return "".join(stack).lstrip("0") or "0"


if __name__ == "__main__":
    print(f"Smallest number: {remove_k_digits(number, k)}")