# Leetcode Problem 113: Path Sum II


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def path_sum_ii(root, target):
    """Return every root-to-leaf path whose values sum to target."""
    result = []

    def visit(node, remaining, path):
        if not node:
            return
        path.append(node.value)
        if not node.left and not node.right and remaining == node.value:
            result.append(path[:])
        visit(node.left, remaining - node.value, path)
        visit(node.right, remaining - node.value, path)
        path.pop()

    visit(root, target, [])
    return result


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4), TreeNode(8))
    print(f"Matching paths: {path_sum_ii(root, 9)}")