# Leetcode Problem 104: Maximum Depth of Binary Tree


class TreeNode:
    """A node in a binary tree."""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maximum_depth(root):
    """
    Find the number of nodes on the longest root-to-leaf path.

    Parameters:
    root (TreeNode): The root of a binary tree.

    Returns:
    int: The tree's maximum depth.
    """
    if not root:
        return 0
    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = maximum_depth(root)
    print(f"Maximum tree depth: {result}")