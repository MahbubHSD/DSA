# Leetcode Problem 297: Serialize and Deserialize Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(root):
    """
    Serialize a binary tree using preorder traversal.

    Parameters:
    root (TreeNode): The tree root.

    Returns:
    str: Comma-separated tree values.
    """
    values = []

    def visit(node):
        if not node:
            values.append("#")
            return
        values.append(str(node.value))
        visit(node.left)
        visit(node.right)

    visit(root)
    return ",".join(values)


def deserialize(text):
    """Rebuild a tree from serialize output."""
    values = iter(text.split(","))

    def build():
        value = next(values)
        if value == "#":
            return None
        return TreeNode(int(value), build(), build())

    return build()


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = deserialize(serialize(root))
    print(f"Deserialized root: {result.value}")