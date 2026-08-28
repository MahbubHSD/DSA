# Leetcode Problem 572: Subtree of Another Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_subtree(root, candidate):
    """
    Determine whether candidate occurs as a complete subtree of root.

    Parameters:
    root (TreeNode): The main tree root.
    candidate (TreeNode): The possible subtree root.

    Returns:
    bool: True when candidate is contained in root.
    """
    def same(first, second):
        if not first or not second:
            return first is second
        return first.value == second.value and same(first.left, second.left) and same(first.right, second.right)

    if not candidate:
        return True
    if not root:
        return False
    return same(root, candidate) or is_subtree(root.left, candidate) or is_subtree(root.right, candidate)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    result = is_subtree(root, TreeNode(4, TreeNode(1), TreeNode(2)))
    print(f"Candidate is a subtree: {result}")