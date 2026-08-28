# Leetcode Problem 100: Same Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_same_tree(first, second):
    """
    Determine whether two binary trees have identical structure and values.

    Parameters:
    first (TreeNode): First tree root.
    second (TreeNode): Second tree root.

    Returns:
    bool: True when the trees are identical.
    """
    if not first or not second:
        return first is second
    return first.value == second.value and is_same_tree(first.left, second.left) and is_same_tree(first.right, second.right)


if __name__ == "__main__":
    result = is_same_tree(TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2)))
    print(f"Trees are the same: {result}")