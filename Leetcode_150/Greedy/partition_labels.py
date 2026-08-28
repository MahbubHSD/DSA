# Leetcode Problem 763: Partition Labels

text = "ababcbacadefegdehijhklij"


def partition_labels(text):
    """
    Split text into the largest parts with no character shared between parts.

    Parameters:
    text (str): A lowercase string.

    Returns:
    list: Lengths of the partitions.
    """
    last = {character: index for index, character in enumerate(text)}
    result = []
    start = end = 0
    for index, character in enumerate(text):
        end = max(end, last[character])
        if index == end:
            result.append(end - start + 1)
            start = index + 1
    return result


if __name__ == "__main__":
    result = partition_labels(text)
    print(f"Partition lengths: {result}")