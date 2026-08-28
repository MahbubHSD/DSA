# Leetcode Problem 516: Longest Palindromic Subsequence

text = "bbbab"


def longest_palindromic_subsequence(text):
    """Find the length of the longest palindromic subsequence."""
    previous = [0] * len(text)
    for left in range(len(text) - 1, -1, -1):
        current = [0] * len(text)
        current[left] = 1
        for right in range(left + 1, len(text)):
            current[right] = previous[right - 1] + 2 if text[left] == text[right] else max(previous[right], current[right - 1])
        previous = current
    return previous[-1] if text else 0


if __name__ == "__main__":
    print(f"Longest palindromic subsequence: {longest_palindromic_subsequence(text)}")