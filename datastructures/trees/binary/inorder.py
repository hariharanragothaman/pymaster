"""
Common recipes in Trees
"""
def inorder(node: TreeNode) -> Iterator[int]:
    stack = []

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        yield node.val
        node = node.right