# Leetcode Problem 129: Sum Root to Leaf Numbers


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_root_to_leaf(root):
    """Sum numbers formed by every root-to-leaf digit path."""
    def visit(node, value):
        if not node:
            return 0
        value = value * 10 + node.value
        if not node.left and not node.right:
            return value
        return visit(node.left, value) + visit(node.right, value)

    return visit(root, 0)


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Root-to-leaf sum: {sum_root_to_leaf(root)}")