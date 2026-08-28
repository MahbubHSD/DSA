# Leetcode Problem 124: Binary Tree Maximum Path Sum


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maximum_path_sum(root):
    """
    Find the greatest sum of any path through a binary tree.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    int: Maximum path sum.
    """
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0
        left = max(0, gain(node.left))
        right = max(0, gain(node.right))
        best = max(best, node.value + left + right)
        return node.value + max(left, right)

    gain(root)
    return best


if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = maximum_path_sum(root)
    print(f"Maximum path sum: {result}")