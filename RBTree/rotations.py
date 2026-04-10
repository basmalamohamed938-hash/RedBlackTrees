def rotate_left(tree, node):
    """Left rotation around the given node."""
    right_child = node.right
    node.right = right_child.left

    if right_child.left != tree.NULL_LEAF:
        right_child.left.parent = node

    right_child.parent = node.parent

    if node.parent is None:
        tree.root = right_child
    elif node == node.parent.left:
        node.parent.left = right_child
    else:
        node.parent.right = right_child

    right_child.left = node
    node.parent = right_child


def rotate_right(tree, node):
    """Right rotation around the given node."""
    left_child = node.left
    node.left = left_child.right

    if left_child.right != tree.NULL_LEAF:
        left_child.right.parent = node

    left_child.parent = node.parent

    if node.parent is None:
        tree.root = left_child
    elif node == node.parent.right:
        node.parent.right = left_child
    else:
        node.parent.left = left_child

    left_child.right = node
    node.parent = left_child