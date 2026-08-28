# Leetcode Problem 543: Diameter of Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def diameter_of_tree(root):
    """
    Find the longest path between any two tree nodes in edges.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    int: The tree diameter measured in edges.
    """
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = diameter_of_tree(root)
    print(f"Tree diameter: {result}")