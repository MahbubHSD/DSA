# Leetcode Problem 802: Find Eventual Safe States

graph = [[1, 2], [2, 3], [5], [0], [5], [], []]


def eventual_safe_states(graph):
    """Return nodes that eventually reach terminal nodes, in sorted order."""
    state = [0] * len(graph)

    def safe(node):
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True
        state[node] = 1
        if all(safe(neighbor) for neighbor in graph[node]):
            state[node] = 2
            return True
        return False

    return [node for node in range(len(graph)) if safe(node)]


if __name__ == "__main__":
    print(f"Safe states: {eventual_safe_states(graph)}")