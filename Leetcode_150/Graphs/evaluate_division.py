# Leetcode Problem 399: Evaluate Division

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["c", "a"]]


def evaluate_division(equations, values, queries):
    """
    Evaluate division queries using weighted graph traversal.

    Parameters:
    equations (list): Variable pairs representing division equations.
    values (list): Quotients corresponding to equations.
    queries (list): Variable pairs to evaluate.

    Returns:
    list: Query results, or -1.0 when no path exists.
    """
    graph = {}
    for (first, second), value in zip(equations, values):
        graph.setdefault(first, []).append((second, value))
        graph.setdefault(second, []).append((first, 1 / value))

    def find(first, second):
        if first not in graph or second not in graph:
            return -1.0
        stack = [(first, 1.0)]
        seen = {first}
        while stack:
            node, product = stack.pop()
            if node == second:
                return product
            for neighbor, ratio in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append((neighbor, product * ratio))
        return -1.0

    return [find(first, second) for first, second in queries]


if __name__ == "__main__":
    result = evaluate_division(equations, values, queries)
    print(f"Division results: {result}")