# Leetcode Problem 226: Invert Binary Tree


class TreeNode:
    """A node in a binary tree."""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def invert_tree(root):
    """
    Swap the left and right children of every tree node.

    Parameters:
    root (TreeNode): The root of a binary tree.

    Returns:
    TreeNode: The root of the inverted tree.
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result = invert_tree(root)
    print(f"Inverted root children: {result.left.value}, {result.right.value}")