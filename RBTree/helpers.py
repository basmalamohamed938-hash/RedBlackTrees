from model  import RBNode

def create_null_leaf():
    """Create a sentinel NULL leaf node."""
    null_leaf = RBNode(None)
    null_leaf.color = 'BLACK'
    null_leaf.left = None
    null_leaf.right = None
    null_leaf.parent = None
    return null_leaf

def bst_insert(tree, root, node):
    """Standard BST insertion."""
    if node.data < root.data:
        if root.left == tree.NULL_LEAF:
            root.left = node
            node.parent = root
        else:
            bst_insert(tree, root.left, node)
    else:
        if root.right == tree.NULL_LEAF:
            root.right = node
            node.parent = root
        else:
            bst_insert(tree, root.right, node)