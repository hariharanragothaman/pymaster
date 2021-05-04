def paths(root):
    if not root:
        return []
    stack = [(root, [root.val])]
    paths = []

    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + [node.left.val]))
        if node.right:
            stack.append((node.right, path + [node.right.val]))
    print(paths)
