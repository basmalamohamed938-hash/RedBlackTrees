from model.RBNode import RBNode
from .helpers import bst_insert
from .fix_insert import fix_insert

def insert(tree, value):
    """Insert a new value into the Red-Black Tree."""
    new_node = RBNode(value)
    new_node.left = tree.NULL_LEAF
    new_node.right = tree.NULL_LEAF
    new_node.color = 'RED'

    if tree.root is None:
        tree.root = new_node
        new_node.parent = None
    else:
        bst_insert(tree, tree.root, new_node)

    fix_insert(tree, new_node)