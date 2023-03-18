# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Rodrigo, Augusto, Danial, Fernando
"""

class Empty(Exception): pass


class ArrayDequeMaxlen(): 

# parameter max len
    def __init__(self):
        pass
        
# We should implement the following methods:

# D.add_first(e): Add element e to the front of deque D.
    def add_first(self, element):
        pass

# D.add_last(e): Add element e to the back of deque D.
    def add_last(self, element):
        pass
    
# D.delete_first(): Remove and return the fist element from deque D
    def delete_first(self):
        pass
    
# D.first(): Return the first element of deque D
    def first(self):
        pass
    
# D.last(): Return the last element of deque D
    def last(self):
        pass
    
# D.is_empty(): Return True if deque D does not contain any elements.
    def is_empty(self):
        pass
    
# len(D): Return the number of elements in deque D    
    def len(self):
        pass   