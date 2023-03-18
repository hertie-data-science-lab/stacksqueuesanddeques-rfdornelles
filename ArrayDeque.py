# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Rodrigo, Augusto, Danial, Fernando
"""

class Empty(Exception): pass


class ArrayDequeMaxlen(): 

# parameter max len
    def __init__(self, max_len = 5):
        print(f"Constructing a deque of size {max_len}")
        self._data = [None] * max_len 
        self._size = 0
        self._cap = max_len

# helper to update the size
    def __update_size__(self):
        count = 0
        
        for element in self._data:
            
            if element is not None:
                count += 1
        self._size = count
        return count

# helper to return the X element of the deque
    def _get_element_(self, n):
        pass

# D.is_empty():1 Return True if deque D does not contain any elements.
    def is_empty(self):
        
        return self.__update_size__() == 0
    
# len(D): Return the number of elements in deque D    
    def len(self):
        return self.__update_size__()
        
# We should implement the following methods:

# D.add_first(e): Add element e to the front of deque D.
    def add_first(self, element):
        self.__update_size__()
        
        new_data = [element]
        new_data.append(self._data[0])
        
        for i in range(1, self._cap - 1):
            new_data.append(self._data[i])

        self._data = new_data
            

# D.add_last(e): Add element e to the back of deque D.
    def add_last(self, element):
        self.__update_size__()
        size = self._cap
        
        new_data = [None] * size         
        new_data[size - 1] = element
        
        for i in reversed(range(self._cap-1)): 
            new_data[i] = self._data[i+1]
            
        self._data = new_data
        
# D.first(): Return the first element of deque D
    def first(self):
        return self._data[0]
        
# D.delete_first(): Remove and return the fist element from deque D
    def delete_first(self):
        self.__update_size__()
        
        first_element = self.first()
        self.add_last(None)
        return first_element
    

# D.last(): Return the last element of deque D
    def last(self):
        return self._data[self._cap - 1]
    
## tests

print("Testing...")
D = ArrayDequeMaxlen(20)

print(D._data)
print(D._cap)

print("add first\n")
D.add_first("1")
D.add_first(2)
D.add_first("3")

print(D._data)

print("size:", D.len())
print("first:", D.first())
print("last:", D.last())

print("add last\n")
D.add_last("a")
D.add_last("b")

print(D._data)

print("size:", D.len())
print("first:", D.first())
print("last:", D.last())

print("first:", D.delete_first())
print(D._data)