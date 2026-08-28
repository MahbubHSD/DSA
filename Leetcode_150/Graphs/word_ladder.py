# Leetcode Problem 127: Word Ladder

begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]


def word_ladder(begin_word, end_word, word_list):
    """
    Find the shortest one-letter transformation sequence.

    Parameters:
    begin_word (str): Starting word.
    end_word (str): Target word.
    word_list (list): Allowed intermediate words.

    Returns:
    int: Sequence length, or zero if no transformation exists.
    """
    from collections import deque

    words = set(word_list)
    if end_word not in words:
        return 0
    queue = deque([(begin_word, 1)])
    while queue:
        word, distance = queue.popleft()
        if word == end_word:
            return distance
        for index in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                candidate = word[:index] + letter + word[index + 1:]
                if candidate in words:
                    words.remove(candidate)
                    queue.append((candidate, distance + 1))
    return 0


if __name__ == "__main__":
    result = word_ladder(begin_word, end_word, word_list)
    print(f"Word ladder length: {result}")