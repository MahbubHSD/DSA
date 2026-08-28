# Leetcode Problem 14: Longest Common Prefix

words = ["flower", "flow", "flight"]


def longest_common_prefix(words):
    """
    Find the longest prefix shared by every word.

    Parameters:
    words (list): A list of strings.

    Returns:
    str: Shared prefix, or an empty string.
    """
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    result = longest_common_prefix(words)
    print(f"Common prefix: {result}")