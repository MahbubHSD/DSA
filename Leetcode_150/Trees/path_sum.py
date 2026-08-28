# Leetcode Problem 112: Path Sum


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def has_path_sum(root, target):
    """
    Determine whether a root-to-leaf path totals target.

    Parameters:
    root (TreeNode): The tree root.
    target (int): Required path sum.

    Returns:
    bool: True when a matching root-to-leaf path exists.
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.value == target
    return has_path_sum(root.left, target - root.value) or has_path_sum(root.right, target - root.value)


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4), TreeNode(8))
    result = has_path_sum(root, 9)
    print(f"Has target path: {result}")