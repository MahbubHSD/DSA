# Leetcode Problem 102: Binary Tree Level Order Traversal


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root):
    """
    Return tree values grouped by depth from top to bottom.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    list: Values grouped into level lists.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = level_order(root)
    print(f"Level order: {result}")