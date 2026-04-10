class RBNode:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # New nodes are always red
        self.left = None
        self.right = None
        self.parent = None

    def search(self, element, root):
        if not root:
            return "NO"
        if element == root.value:
            result = "YES"
        elif element < root.value:
            return self.search(element,root.left)
        else:
            return self.search(element,root.right)

    def calculateSize(self, root):
        if not root:
            return 0
        return 1 + self.calculateSize(root.left) + self.calculateSize(root.right)

    def calculateHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.calculateHeight(root.left), self.calculateHeight(root.right))
    
    def calculateBlackHeight(self, root):
        if not root:
            return 0
        if root.color == 1:
            return 1 + self.calculateBlackHeight(root.left) + self.calculateBlackHeight(root.right)
        else:
            self.calculateBlackHeight(root.left) + self.calculateBlackHeight(root.right)
