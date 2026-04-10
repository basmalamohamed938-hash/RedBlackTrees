def get_size(root):
    if not root:
        return 0
    return 1 + get_size(root.left) + get_size(root.right)

def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))
    
def get_black_height(root):
    if not root:
        return 0
    if root.color == 1:
        return 1 + get_black_height(root.left) + get_black_height(root.right)
    else:
        get_black_height(root.left) + get_black_height(root.right)