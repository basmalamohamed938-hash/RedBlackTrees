from .helpers import create_null_leaf
from .insert import insert
from .search import search
from .rotations import rotate_left, rotate_right
from .fix_insert import fix_insert
from .height import get_height, calculate_height
from .black_height import get_black_height, calculate_black_height
from .size import get_size, calculate_size

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
        return search(self, value)
    
    def get_height(self):
        return get_height(self)
    
    def get_black_height(self):
        return get_black_height(self)
    
    def get_size(self):
        return get_size(self)
    
    def get_root(self):
        return self.root