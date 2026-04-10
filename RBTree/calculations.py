def get_size(root):
    if root is None or root.data is None:
        return 0
    return 1 + get_size(root.left) + get_size(root.right)

def get_height(root):
    if root is None or root.data is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))
    
def get_black_height(root):
    if not root or root.data is None:
        return 0
    if root.color == 'BLACK':
        return 1 + get_black_height(root.left) + get_black_height(root.right)
    else:
        return get_black_height(root.left) + get_black_height(root.right)