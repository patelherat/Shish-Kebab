"""
Everything needed to do the graphical Shish Kebab.  This is a fully object
oriented class with a constructor and methods, utilizing the 'self' concept
for the instance name.

Author: Sean Strout @ RIT CS
"""
from graphics import GraphWin, Line, Point, Circle, Rectangle

# This dictionary maps food items (string), to colors (string)
COLORS = {
    "beef": "red4",
    "chicken": "yellow2",
    "onion": "purple",
    "pepper": "green",
    "tomato": "red",
    "pork": "pink",
    "mushroom": "tan",
}

# global constants for drawing
WIN_HEIGHT = 1
WIN_LOW_LEFT_X = -1
WIN_LOW_LEFT_Y = 0
WIN_UP_RIGHT_Y = WIN_LOW_LEFT_Y + WIN_HEIGHT
LINE_THICKNESS = 2
FOOD_WIDTH = 1
SKEWER_HANDLE_RADIUS = 0.1
BKGD_COLOR = "white"

class SkewerUI(object):
    """
    Class: SkewerUI
    Description: A graphical display for the Skewer. It displays
        the items in on the skewer graphically, as they are added,
        removed and shifted around by the various commands.
    """

    __slots__ = ( 
        'win',          # the graphical window
        'items'         # the list of food items (strings) from top to bottom
    )

    def __init__( self, capacity ):
        """
         Create the SkewerUI.
        :param capacity: the capacity of the skewer (for the window size)
        """

        # create the window
        self.create_window(capacity) # (Sets value of win attribute.)
        self.items = []
    
    def close(self):
        """
        On destruction, close the graphical window.
        :param self: the SkewerUI being closed
        """
        
        self.win.close()
    
    def create_window(self, capacity):
        """
        Create the graphics window.
        :param capacity: the capacity of the skewer (for the window size)
        :return: None
        """

        self.win = GraphWin("Shish Kebab", 800, 200)
        self.win.setCoords( 
            WIN_LOW_LEFT_X, 
            WIN_LOW_LEFT_Y - 0.1, 
            WIN_LOW_LEFT_X+(capacity+1)*FOOD_WIDTH,
            WIN_UP_RIGHT_Y + 0.1 
        )
        
        # draw skewer
        line = Line( 
            Point(WIN_LOW_LEFT_X, WIN_LOW_LEFT_Y+WIN_HEIGHT/2.0), 
            Point(capacity, WIN_LOW_LEFT_Y+WIN_HEIGHT/2.0)
        )
        line.setWidth(LINE_THICKNESS)
        line.draw(self.win)
        handle = Circle( 
            Point(capacity-.1, WIN_LOW_LEFT_Y+WIN_HEIGHT/2.0),
            SKEWER_HANDLE_RADIUS 
        )
        handle.setFill(BKGD_COLOR)
        handle.setWidth(LINE_THICKNESS)
        handle.draw(self.win)
        self.items = []


    class _ShapeInfo():
        """
        Vegetables are circles and meats are rectangles.
        """

        __slots__ = 'shapeClass', 'ctorArgs'

        def __init__( self, shapeClass, ctorArgs ):
            """
            Initialize the ShapeInfo.

            :param shapeClass: shape class
            :param ctorArgs: constructor arguments
            """
            self.shapeClass = shapeClass
            self.ctorArgs = ctorArgs

    Shapes = { 
              True: _ShapeInfo( Circle, ( Point( 0, .5 ), .5 ) ), 
              False: _ShapeInfo( Rectangle, ( Point( -.5, 0 ), Point( .5, 1 ) ) ) 
    } # The bool is for vegetarian

    def add( self, food ):
        """
        Called whenever an item is added to the Skewer, so the graphics
        can be updated.  It uses the KSpot class to get the food items
        and display them.
        :param food: the new food added to the skewer (KebabSpot)
        :return None
        """

        if food != None:
            shapeInfo = SkewerUI.Shapes[ food.item.is_veggie() ]
            graphic = (shapeInfo.shapeClass)( *shapeInfo.ctorArgs )
            graphic.setFill(COLORS[food.item.name])
            graphic.draw( self.win )
            for prev in self.items:
                prev.move( 1, 0 )
            self.items.insert( 0, graphic )
            

    def remove( self ):
        """
        Called whenever an item is removed to the Skewer, so the graphics
        can be updated.  It uses the KSpot class to get the food items
        and display them.
        :param head: the head of the skewer (KSpot)
        :return None
        """
        
        if len( self.items ) != 0:
            self.items[ 0 ].undraw()
            self.items.pop( 0 )
            for prev in self.items:
                prev.move( -1, 0 )
