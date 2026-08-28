# Leetcode Problem 1647: Minimum Deletions to Make Character Frequencies Unique

text = "aaabbbcc"


def minimum_deletions_unique_frequencies(text):
    """Delete the fewest characters so all positive frequencies are unique."""
    from collections import Counter

    used = set()
    deletions = 0
    for frequency in Counter(text).values():
        while frequency and frequency in used:
            frequency -= 1
            deletions += 1
        used.add(frequency)
    return deletions


if __name__ == "__main__":
    print(f"Minimum deletions: {minimum_deletions_unique_frequencies(text)}")