def search(root, element):
    if not root or not root.data:
        return "NO"
    if element == root.data:
        return "YES"
    if element < root.data:
        return search(root.left, element)
    return search(root.right, element)