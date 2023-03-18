# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:01 2023

@author: Rodrigo, Augusto, Danial, Fernando
"""

class Empty(Exception): pass


class ArrayDequeMaxlen(): 
    """ Class to generate a Double-Ended Queue (Deque) ADT, which allows the insertions of data in both sides.
    """
    def __init__(self, max_len = 5):
        """Constructor of the deque without any data and size 0. A maximum lenght shall be defined.

        Args:
            max_len (int, optional): The maximun lenght of the deque. Defaults to 5.
        """
        print(f"Constructing a deque of size {max_len}")
        self._data = [None] * max_len # a list of max_len size, with only empty elements
        self._size = 0 
        self._cap = max_len

# helper to update the size
    def __update_size__(self):
        """Internal function to make sure the self._size object is accurate. 
        It will be called internally only necessary.

        Returns:
            int: the number of non-None elements
        """
        count = 0 # initialize the count with 0
                
        for element in self._data:
            # check if the element is valid (not None)
            if element is not None:
                count += 1 # if it is, add 1
                
        self._size = count # update the value of self._size
        # returns the count of valid elements
        return count 

# D.is_empty():1 Return True if deque D does not contain any elements.
    def is_empty(self):
        """Check if the deque is an empty object, i.e, it has only None elements.

        Returns:
            logical: either True or False
        """
        # calls the update function and checks if it's 0
        return self.__update_size__() == 0
    
# len(D): Return the number of elements in deque D    
    def len(self):
        """Return the size of elements (not the capacity) of the deque. It rellies in the method __update_size__().

        Returns:
            int: the number of not-None elements
        """
        # call the update function and return its numeric value
        return self.__update_size__()

# D.add_first(e): Add element e to the front of deque D.
    def add_first(self, element):
        """Add element to the front of the deque, pushing all other elements to the right. 
        If any element exceeds the deque's capacity it will be removed.

        Args:
            element: The element to be included.
        """
        # generate a new list
        # the first element will be the element received by the function
        new_data = [element]
        # the second element will be the first element of the data
        new_data.append(self._data[0])
        
        # iterate through all other elements, except the last (which will be ignored/removed)
        for i in range(1, self._cap - 1):
            new_data.append(self._data[i])
        
        # update the data
        self._data = new_data
            

# D.add_last(e): Add element e to the back of deque D.
    def add_last(self, element):
        """Adds the element in the last position of the deque. It will push all other elements to the left.
        In case the deque's capacity is reached, the first element will be removed.

        Args:
            element: The element to be included.
        """
        # gets the deque's capacity
        size = self._cap
        
        # creates an empty list of {size} elements
        new_data = [None] * size  
        
        # the last position will be the element received by the function       
        new_data[size - 1] = element
        
        # iterates in the reverse order filling the list with the elements of the original list
        # but it skips in order to ignore/remove the first element if it exceeds the deque's size
        for i in reversed(range(self._cap-1)): 
            new_data[i] = self._data[i+1]
            
        # update the data
        self._data = new_data
        
# D.first(): Return the first element of deque D
    def first(self):
        """Inform (but not remove) the first element of the deque.

        Returns:
            first element
        """
        return self._data[0]
        
# D.delete_first(): Remove and return the fist element from deque D
    def delete_first(self):
        """Return and then remove the first element of the deque.

        Returns:
            element: the first element, that will be removed
        """
        # check which is the first element
        first_element = self.first()
        # add a None element in the deque, pushing all other elements to the left and removing the
        # first element
        self.add_last(None)
        
        # returns the "former" first element
        return first_element
    

# D.last(): Return the last element of deque D
    def last(self):
        """_Inform (but not remove) the last element of the deque.

        Returns:
            element: the last element
        """
        return self._data[self._cap - 1] # the last element in the data
