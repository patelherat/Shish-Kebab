__author__ = 'hap', 'aps'

"""
A module that represents the valid food types.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7
}

# Implement Food class here
class Food:
    """
    Class: Food
    Description: This class contains the food types that can be placed on the skewer. It
            contains the details of the calories of the foods as well which foods are
            veggies.
    """

    __slots__ = "name", "calories"

    def __init__(self, name):
        """
        Construct a Food instance.
        :param name: the name (String) placed at the KebabSpot 
        """
        
        self.name = name
        self.calories = CALORIES.get(name)
        
    def is_veggie(self):
        """
        Return whether this Food item is a veggie or not.
        :return True if this Food item is a veggie, 
        False otherwise.
        """
        
        if self.name in VEGGIES:
            return True
        else:
            return False
