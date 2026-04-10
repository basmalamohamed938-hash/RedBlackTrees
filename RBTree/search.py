def search(root, element):
        if not root:
            return "NO"
        if element == root.value:
            return "YES"
        elif element < root.value:
            return search(element,root.left)
        else:
            return search(element,root.right)