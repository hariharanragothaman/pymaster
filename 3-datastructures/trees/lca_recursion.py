"""
Standard recipe to find the lowest common ancestor
"""


def lca(self, root, a, b):
    # Standard Recipe to find the lowest-common ancestor
    if root is None or root is a or root is b:
        return root
    left = self.lca(root.left, a, b)
    right = self.lca(root.right, a, b)
    if left is not None and right is not None:
        return root
    return left if left else right
