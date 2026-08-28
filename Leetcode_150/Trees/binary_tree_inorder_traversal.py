# Leetcode Problem 94: Binary Tree Inorder Traversal


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Return binary-tree values in left-root-right order."""
    result = []
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.value)
        node = node.right
    return result


if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(f"Inorder values: {inorder_traversal(root)}")