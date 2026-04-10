from .load_file import load_from_file
from .insert_word import insert_word
from .lookup_word import lookup_word
from .print_stats import print_stats

class Dictionary:
    def __init__(self):
        from rbtree import RBTree
        self.tree = RBTree()
    
    def load_from_file(self, filename):
        load_from_file(self, filename)
    
    def insert_word(self, word):
        insert_word(self, word)
    
    def lookup_word(self, word):
        lookup_word(self, word)
    
    def print_stats(self):
        print_stats(self)