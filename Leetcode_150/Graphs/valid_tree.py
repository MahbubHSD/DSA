# Leetcode Problem 261: Graph Valid Tree

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]


def valid_tree(n, edges):
    """
    Determine whether undirected edges form one connected acyclic tree.

    Parameters:
    n (int): Number of nodes labeled from zero through n - 1.
    edges (list): Undirected edges.

    Returns:
    bool: True when the graph is a valid tree.
    """
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for first, second in edges:
        first_root, second_root = find(first), find(second)
        if first_root == second_root:
            return False
        parent[first_root] = second_root
    return True


if __name__ == "__main__":
    result = valid_tree(n, edges)
    print(f"Edges form a tree: {result}")