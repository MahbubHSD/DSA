# Leetcode Problem 105: Construct Binary Tree from Preorder and Inorder Traversal


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    """
    Reconstruct a binary tree from preorder and inorder traversals.

    Parameters:
    preorder (list): Root-first traversal values.
    inorder (list): Left-root-right traversal values.

    Returns:
    TreeNode: The reconstructed tree root.
    """
    positions = {value: index for index, value in enumerate(inorder)}
    preorder_index = 0

    def build(left, right):
        nonlocal preorder_index
        if left > right:
            return None
        value = preorder[preorder_index]
        preorder_index += 1
        node = TreeNode(value)
        middle = positions[value]
        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)
        return node

    return build(0, len(inorder) - 1)


if __name__ == "__main__":
    result = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(f"Constructed root: {result.value}")