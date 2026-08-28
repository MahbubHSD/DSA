# Leetcode Problem 236: Lowest Common Ancestor of a Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lowest_common_ancestor(root, first, second):
    """
    Find the lowest node that has both targets as descendants.

    Parameters:
    root (TreeNode): The binary tree root.
    first (TreeNode): First target node.
    second (TreeNode): Second target node.

    Returns:
    TreeNode: The lowest common ancestor.
    """
    if not root or root is first or root is second:
        return root
    left = lowest_common_ancestor(root.left, first, second) if root.left else None
    right = lowest_common_ancestor(root.right, first, second) if root.right else None
    return root if left and right else left or right


if __name__ == "__main__":
    first = TreeNode(5)
    second = TreeNode(1)
    root = TreeNode(3, first, second)
    result = lowest_common_ancestor(root, first, second)
    print(f"Lowest common ancestor: {result.value}")