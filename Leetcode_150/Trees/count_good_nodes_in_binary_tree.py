# Leetcode Problem 1448: Count Good Nodes in Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_good_nodes(root):
    """
    Count nodes not smaller than every ancestor on their path.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    int: Number of good nodes.
    """
    def count(node, maximum):
        if not node:
            return 0
        good = node.value >= maximum
        maximum = max(maximum, node.value)
        return good + count(node.left, maximum) + count(node.right, maximum)

    return count(root, float("-inf"))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(1), TreeNode(5)))
    result = count_good_nodes(root)
    print(f"Good nodes: {result}")