def search(element, root):
        if not root:
            return "NO"
        if element == root.value:
            result = "YES"
        elif element < root.value:
            return search(element,root.left)
        else:
            return search(element,root.right)