from .rotations import rotate_left, rotate_right

def fix_insert(tree, node):
    """Fix Red-Black Tree properties after insertion."""
    while node != tree.root and node.parent.color == 'RED':
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            
            if uncle.color == 'RED':
                # Case 1: Uncle is red - recolor
                node.parent.color = 'BLACK'
                uncle.color = 'BLACK'
                node.parent.parent.color = 'RED'
                node = node.parent.parent
            else:
                # Case 2 & 3: Uncle is black
                if node == node.parent.right:
                    # Case 2: node is right child - left rotate
                    node = node.parent
                    rotate_left(tree, node)
                
                # Case 3: node is left child - right rotate
                node.parent.color = 'BLACK'
                node.parent.parent.color = 'RED'
                rotate_right(tree, node.parent.parent)
        else:
            # Mirror case (parent is right child)
            uncle = node.parent.parent.left
            
            if uncle.color == 'RED':
                node.parent.color = 'BLACK'
                uncle.color = 'BLACK'
                node.parent.parent.color = 'RED'
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    rotate_right(tree, node)
                
                node.parent.color = 'BLACK'
                node.parent.parent.color = 'RED'
                rotate_left(tree, node.parent.parent)
    
    tree.root.color = 'BLACK'