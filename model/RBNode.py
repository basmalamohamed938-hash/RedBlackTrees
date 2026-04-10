class RBNode:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # New nodes are always red
        self.left = None
        self.right = None
        self.parent = None