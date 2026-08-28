# Leetcode Problem 131: Palindrome Partitioning

text = "aab"


def palindrome_partitioning(text):
    """
    Split text into every possible list of palindromic substrings.

    Parameters:
    text (str): The string to partition.

    Returns:
    list: All valid palindrome partitions.
    """
    result = []

    def search(start, current):
        if start == len(text):
            result.append(current[:])
            return
        for end in range(start + 1, len(text) + 1):
            part = text[start:end]
            if part == part[::-1]:
                search(end, current + [part])

    search(0, [])
    return result


if __name__ == "__main__":
    result = palindrome_partitioning(text)
    print(f"Palindrome partitions: {result}")