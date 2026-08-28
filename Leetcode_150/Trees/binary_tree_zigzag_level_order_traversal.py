# Leetcode Problem 103: Binary Tree Zigzag Level Order Traversal


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_level_order(root):
    """
    Return tree levels alternating left-to-right and right-to-left.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    list: Zigzag-ordered level values.
    """
    if not root:
        return []
    result = []
    queue = [root]
    reverse = False
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level[::-1] if reverse else level)
        reverse = not reverse
    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = zigzag_level_order(root)
    print(f"Zigzag levels: {result}")