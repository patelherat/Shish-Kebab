__author__ = 'hap', 'aps'

"""
A module that represents "spots" on the skewer.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """

    __slots__ = "item", "next"

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """
        
        self.item = item
        self.next = next
        
        pass

    def size(self):    #########################
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        
        count = 0
        if self.next:
            count = self.next.size()
        count+=1
        return count

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """

        if not self.item.is_veggie():
            return False
        elif self.next:
            if not self.next.is_vegan():
                return False
        return True

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """

        if self.item.name == name:
            return True
        elif self.next:
            if self.next.has(name):
                return True
        return False

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """

        if self.next:
            items = self.item.name + ", " + self.next.string_em()
        else:
            items = self.item.name
        
        return items

    def get_item(self):
        """
        Return the Food object stored as item in this spot.
        :return The Food object.
        """
        return self.item

    def calories(self):
        """
        Return the total calories uptil this spot from the end of the skewer.
        :return total calories uptil this spot from the end.
        """

        calorie = self.item.calories
        if self.next:
            calorie += self.next.calories()
        return calorie
