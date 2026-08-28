# Leetcode Problem 637: Average of Levels in Binary Tree


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def average_of_levels(root):
    """Return the average value of every binary-tree level."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        values = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(sum(values) / len(values))
    return result


if __name__ == "__main__":
    print(f"Level averages: {average_of_levels(TreeNode(3, TreeNode(9), TreeNode(20)))}")