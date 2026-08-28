# Leetcode Problem 797: All Paths From Source to Target

graph = [[1, 2], [3], [3], []]


def all_paths_source_target(graph):
    """Return every path from node zero to the final node."""
    target = len(graph) - 1
    result = []

    def visit(node, path):
        if node == target:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            visit(neighbor, path + [neighbor])

    visit(0, [0])
    return result


if __name__ == "__main__":
    print(f"All paths: {all_paths_source_target(graph)}")