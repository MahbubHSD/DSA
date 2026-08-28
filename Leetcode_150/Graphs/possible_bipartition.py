# Leetcode Problem 886: Possible Bipartition

n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]


def possible_bipartition(n, dislikes):
    """Determine whether people can be split so no disliked pair shares a group."""
    graph = [[] for _ in range(n + 1)]
    for first, second in dislikes:
        graph[first].append(second)
        graph[second].append(first)
    colors = {}
    for start in range(1, n + 1):
        if start in colors:
            continue
        colors[start] = 0
        queue = [start]
        for person in queue:
            for neighbor in graph[person]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[person]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[person]:
                    return False
    return True


if __name__ == "__main__":
    print(f"Possible bipartition: {possible_bipartition(n, dislikes)}")