# Leetcode Problem 230: Kth Smallest Element in a BST


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """
    Find the kth smallest value in a binary search tree.

    Parameters:
    root (TreeNode): A BST root.
    k (int): One-based rank in sorted order.

    Returns:
    int: The kth smallest value.
    """
    stack = []
    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.value
        node = node.right


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    result = kth_smallest(root, 1)
    print(f"Kth smallest value: {result}")