from .helpers import create_null_leaf
from .insert import insert
from .search import search
from .rotations import rotate_left, rotate_right
from .fix_insert import fix_insert
from .calculations import get_height, get_black_height, get_size

class RBTree:
    def __init__(self):
        from .helpers import create_null_leaf
        self.root = None
        self.NULL_LEAF = create_null_leaf()
    
    # Student 1 functions
    def insert(self, value):
        insert(self, value)
    
    # Student 2 functions
    def search(self, value):
        return search(self.root, value)
    
    def get_height(self):
        return get_height(self.root)
    
    def get_black_height(self):
        return get_black_height(self.root)
    
    def get_size(self):
        return get_size(self.root)
    
    def get_root(self):
        return self.root