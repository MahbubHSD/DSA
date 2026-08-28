# Leetcode Problem 133: Clone Graph


class Node:
    def __init__(self, value=0, neighbors=None):
        self.value = value
        self.neighbors = neighbors or []


def clone_graph(node):
    """
    Deep-copy a connected undirected graph.

    Parameters:
    node (Node): A node in the graph.

    Returns:
    Node: The cloned graph's corresponding node.
    """
    if not node:
        return None
    clones = {}

    def clone(current):
        if current in clones:
            return clones[current]
        copy = Node(current.value)
        clones[current] = copy
        copy.neighbors = [clone(neighbor) for neighbor in current.neighbors]
        return copy

    return clone(node)


if __name__ == "__main__":
    node = Node(1)
    node.neighbors = [node]
    result = clone_graph(node)
    print(f"Cloned node value: {result.value}")