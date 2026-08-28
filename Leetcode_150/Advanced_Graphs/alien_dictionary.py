# Leetcode Problem 269: Alien Dictionary

words = ["wrt", "wrf", "er", "ett", "rftt"]


def alien_order(words):
    """
    Derive a valid character order from an alien sorted dictionary.

    Parameters:
    words (list): Words sorted in alien lexicographic order.

    Returns:
    str: A valid character order, or an empty string if invalid.
    """
    from collections import deque

    graph = {character: set() for word in words for character in word}
    indegree = {character: 0 for character in graph}
    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second):
            return ""
        for left, right in zip(first, second):
            if left != right:
                if right not in graph[left]:
                    graph[left].add(right)
                    indegree[right] += 1
                break
    queue = deque(character for character in indegree if indegree[character] == 0)
    order = []
    while queue:
        character = queue.popleft()
        order.append(character)
        for neighbor in graph[character]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return "".join(order) if len(order) == len(graph) else ""


if __name__ == "__main__":
    result = alien_order(words)
    print(f"Alien character order: {result}")