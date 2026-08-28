# Leetcode Problem 72: Edit Distance

first_word = "horse"
second_word = "ros"


def edit_distance(first_word, second_word):
    """
    Find the minimum insertions, deletions, and substitutions needed.

    Parameters:
    first_word (str): The source word.
    second_word (str): The target word.

    Returns:
    int: Minimum edit count.
    """
    previous = list(range(len(second_word) + 1))
    for first_index, first_character in enumerate(first_word, 1):
        current = [first_index]
        for second_index, second_character in enumerate(second_word, 1):
            if first_character == second_character:
                current.append(previous[second_index - 1])
            else:
                current.append(1 + min(previous[second_index], current[-1], previous[second_index - 1]))
        previous = current
    return previous[-1]


if __name__ == "__main__":
    result = edit_distance(first_word, second_word)
    print(f"Edit distance: {result}")