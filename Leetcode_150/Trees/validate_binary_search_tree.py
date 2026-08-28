# Leetcode Problem 98: Validate Binary Search Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root):
    """
    Determine whether a binary tree satisfies BST ordering.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    bool: True if every node is within its valid bounds.
    """
    def validate(node, lower, upper):
        if not node:
            return True
        if not lower < node.value < upper:
            return False
        return validate(node.left, lower, node.value) and validate(node.right, node.value, upper)

    return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = is_valid_bst(root)
    print(f"Tree is a valid BST: {result}")