__author__ = 'hap', 'aps'

"""
The main module for running the Shish Kebab program.

Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

import sys
from food import FOODS
from skewer import Skewer
from skewer_exception import SkewerException

class Kebab:
    """
    Class: Kebab
    Description: This class contains the main loop for the program.  It
        filters the command line input and then calls a Skewer instance
        to deal with the appropriate action.
    """

    __slots__ = "skewer",

    def __init__(self):
        """Create a Kebab instance."""

        # initially there is no skewer until one is created by command.
        self.skewer = None

    def usage(self):
        """
        Displays the valid commands and their usage.
        :return: None
        """

        print("Kebab commands:")
        print("add item - adds an item to the skewer")
        print("calories - get the total number of calories of items on the skewer")
        print("create N - creates a skewer to hold N items")
        print("destroy - destroys the current skewer")
        print("display - displays all the items on the skewer, in order")
        print("eat - eat the front item on the skewer")
        print("foods - display the food items that can be added to the skewer")
        print("front - the front item on the skewer")
        print("has item - is an item on the skewer?")
        print("quit - exit the program")
        print("status - the capacity and current number of items on the skewer")
        print("vegan - does the skewer have any meat?")

    def create(self, args):
        """
        Create the skewer that will hold the food.
        :param args: a string containing the size to create
        :return: None
        """

        try:
            # make sure the size is valid
            if len(args) == 0 or int(args[0]) < 1:
                raise SkewerException("Skewer size must be greater than 0")

            size = int(args[0])

            # force close a pre-existing skewer
            if self.skewer != None:
                self.skewer.close()

            self.skewer = Skewer(size)
            print("Skewer created.")
        except SkewerException as e:
            print(e)
            self.skewer = None
        except Exception as e:
            sys.stderr.write(e)
            self.usage()
            return

    def add(self, args):
        """
        Add a specified item to the skewer.
        :param args: the name of the item to add
        :return: None
        """

        if len(args) < 1: 
            self.usage()
            return

        name = args[0]
        
        # check that the name is in the list of valid foods
        if name not in FOODS:
            print ("Skewer can only hold these kinds of food: ", FOODS)
            return
        try:
            self.skewer.add(name)
            print (name, "successfully added to the skewer.")
        except SkewerException as e:
            print(e)

    def calories(self, args):
        """
        Print the total calories on the skewer.
        :return: None
        """
        
        calorie = self.skewer.calories()
        print ("The skewer has", calorie, "calories.")
        
        
    def eat(self, args):
        """
        Eat the front item on the skewer.
        :param args: ignored
        :return: None
        """

        try:
            name = self.skewer.front()
            self.skewer.remove()
            print("Ate", name, ". Yum!")
        except SkewerException as e:
            print(e)

    def has(self, args):
        """
        Checks if the skewer holds a certain item.
        :param args: the name of the item to search for
        :return: None
        """

        if len(args) < 1: 
            self.usage()
            return

        name = args[0]
        if self.skewer.has(name): 
            print(name, "does exist on the Skewer.")
        else: 
            print(name, "doesn't exist on the Skewer.")

    def status(self, args):
        """
        Displays the number of items on the skewer and its capacity.
        :param args: ignored
        :return: None
        """

        print(str(self.skewer.size()), "out of", self.skewer.capacity(),
            "items on the skewer.")
            
    def front(self, args):
        """
        Displays the name of the front item on the skewer.
        :param args: ignored
        :return: None
        """

        try:
            print(self.skewer.front(), "is on the front of the skewer.")
        except SkewerException as e:
            print(e)
                    
    def display(self, args):
        """
        Displays the items on the skewer by name.
        :param args: ignored
        :return: None
        """

        print("The skewer contains: ", self.skewer)

    def vegan(self, args):
        """
        Displays whether all items on the skewer are vegetarian or not.
        :param args: ignored
        :return: None
        """
        
        if self.skewer.is_vegan():
            print("The skewer is vegan friendly.")
        else:
            print("The skewer contains meat.")

    def foods(self, args):
        """
        Display the valid food items that can be added to the skewer
        :param args: ignored
        :return: None
        """
        print(FOODS)

    def destroy(self, args):
        """
        Destroys the skewer if one was previously created.
        :param args: ignored
        :return: None
        """

        if self.skewer:
            self.skewer.close()
            self.skewer = None

    def quit(self, args):
        """
        Exit the program
        :param args: ignored
        :return: None
        """

        if self.skewer:
            self.skewer.close()
        print("Goodbye!")
        sys.exit(0)

    def main_loop(self):
        """
        Runs the main command loop by prompting for input and responding.
        :return: None
        """

        # Each valid command is stored in a dictionary as string by key.
        # The corresponding method to call is stored as the value.
        CMDS = {"add": self.add,
                "calories": self.calories,
                "create": self.create,
                "destroy": self.destroy,
                "eat": self.eat,
                "foods" : self.foods,
                "has": self.has,
                "status": self.status,
                "front": self.front,
                "display": self.display,
                "vegan": self.vegan,
                "quit": self.quit}

        # the command line prompt
        PROMPT = "> "

        # the command loop runs until the user enters the quit command
        while sys.stdin:
            line = input(PROMPT).split()
            cmd = line[0]
            if cmd in CMDS:
                # if the skewer does not exist, the only valid commands
                # are to create it, list the food items, or quit
                if not self.skewer and cmd != "create" and cmd != "foods" and cmd != "quit":
                    print("Skewer has not been created yet.")
                else:
                    # strip off the command and pass the remaining line
                    # arguments to the appropriate method
                    CMDS[cmd](line[1:])
            else:
                self.usage()

def main():
    """The main routine."""
    
    # create a Kebab instance and invoke the main loop
    kebab = Kebab()
    kebab.main_loop()

if __name__ == "__main__":
    main()
