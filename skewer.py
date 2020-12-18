__author__ = 'hap', 'aps'

"""
A module for representing the skewer functionality.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

from food import Food
from kebab_graphics import SkewerUI
from kebab_spot import KebabSpot
from skewer_exception import SkewerException

class Skewer:
    """
    Class: Skewer
    Description: This class receives commands from Kebab and
        works with the KebabSpot class to represent a shish-kebab
        of food items on a skewer.
    """

    __slots__ = "top", "cap", "ui"

    def __init__(self, capacity):
        """
        Construct a Skewer instance.
        :param capacity: the maximum number of items it can hold
        :exception SkewerException: a capacity less than 1 was specified.
        """
        
        if capacity < 1:
            raise SkewerException("Cannot create skewer!")

        self.top = None
        self.cap = capacity
        self.ui = SkewerUI(self.cap)
        

    def add(self, name):
        """
        Add a food item to the skewer
        :param name: the string name of the food item
        :exception SkewerException: item could not be added.
        :return None
        """
        
        if not self.top or self.top.size() < self.cap:
            self.top = KebabSpot( Food(name), self.top )
            self.ui.add(self.top)
        else:
            raise SkewerException("Cannot add item to a full skewer!")
            
    def front(self):
        """
        Gets the name of the front item on the skewer.
        :exception SkewerException: no item was on the skewer
        :return the name of the food item (string) on the front
        """
        
        if not self.top or self.size() == 0: 
            raise SkewerException("Cannot get item from an empty skewer!")
        return self.top.get_item().name
    
    def remove(self):
        """
        Remove the front item from the skewer.
        :exception: SkewerException: no item was on the skewer
        :return None
        """
        
        if not self.top or self.size() == 0:
            raise SkewerException("Cannot get item from an empty skewer!")
        self.ui.remove()
        self.top = self.top.next

    def size(self):
        """
        Get the number of elements on the skewer.
        :return the number of elements (int)
        """

        if not self.top:
            return 0
        else:
            return self.top.size()
    
    def capacity(self):
        """
        Get the maximum capacity of the skewer.
        :return the capacity (int)
        """

        return self.cap

    def close(self):
        """
        On destruction, close the graphical window.
        :return None
        """

        self.ui.close()

    def is_vegan( self ):
        """
        Are there only vegetables on the skewer?
        :return True if there are only veggies on the skewer, False if not
        """

        if not self.top:
            return True
        else:
            return self.top.is_vegan()

    def has(self, name):
        """
        Is a particular food item on the skewer?
        :param name: the name (string) of the food item to search for
        :return True if the item is on the skewer, False if not.
        """
        
        if not self.top:
            return False
        else:
            return self.top.has( name )

    def __str__( self ):
        """
        Print a string representation of the items on the skewer.
        :return A string containing all the items on the skewer, from front
        to back, comma separated, and surrounded with square brackets
        """
        
        if self.top:
            return "[ " + self.top.string_em() + " ]"
        else:
            return "[]"


    def calories(self):
        """
        Get the total calories on the skewer.
        :return: Value of total calories.
        """
        
        if not self.top:
            return 0
        else:
            return self.top.calories()
