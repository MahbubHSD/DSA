# Leetcode Problem 110: Balanced Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Determine whether subtree heights differ by at most one everywhere.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    bool: True when the tree is height-balanced.
    """
    def height(node):
        if not node:
            return 0
        left, right = height(node.left), height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


if __name__ == "__main__":
    result = is_balanced(TreeNode(3, TreeNode(9), TreeNode(20)))
    print(f"Tree is balanced: {result}")