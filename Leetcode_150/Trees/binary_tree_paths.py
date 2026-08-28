# Leetcode Problem 257: Binary Tree Paths


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_paths(root):
    """Return every root-to-leaf path as an arrow-separated string."""
    result = []

    def visit(node, path):
        if not node:
            return
        path = path + [str(node.value)]
        if not node.left and not node.right:
            result.append("->".join(path))
            return
        visit(node.left, path)
        visit(node.right, path)

    visit(root, [])
    return result


if __name__ == "__main__":
    print(f"Tree paths: {binary_tree_paths(TreeNode(1, TreeNode(2), TreeNode(3)))}")