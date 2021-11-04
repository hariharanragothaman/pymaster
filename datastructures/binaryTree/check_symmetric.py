class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def isSymmetric(root: Node) -> bool:
    """
    Check if left sub-tree and right-subtree are mirror images of each other
    Using standard DFS approach
    """
    if root is None:
        return True

    stack = [[root.left, root.right]]

    while stack:
        left, right = stack.pop()

        if left is None and right is None:
            continue

        if left is None or right is None:
            return False

        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        else:
            return False
    return True
