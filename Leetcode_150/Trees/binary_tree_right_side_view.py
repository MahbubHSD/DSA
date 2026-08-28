# Leetcode Problem 199: Binary Tree Right Side View


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def right_side_view(root):
    """
    Return the node visible at each level from the right side.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    list: Rightmost value at every depth.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        result.append(queue[-1].value)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    result = right_side_view(root)
    print(f"Right side view: {result}")