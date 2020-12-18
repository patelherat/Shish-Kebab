"""
A module containing the exception class for things that can go wrong while
working with the skewer.

Author: Sean Strout @ RITCS
"""

class SkewerException(Exception):
    """
    Class: SkewerException
    Description: Used to represent the various exceptions that can
        happen when dealing with the skewer.
    """

    __slots__ = tuple()

    def __init__(self, msg):
        """
        Construct an exception.
        :param  msg: the message (string) associated with the exception
        """
        self.msg = msg
        
    def __str__(self):
        """
        Get the exception message.
        Arguments:
            self - SkewerException instance being created
        Returns: the message (string) associated with the exception.
        """
        return self.msg