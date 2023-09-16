#!/usr/bin/python3

class Base:
    """implements a class Base
    Private class attribute:
      __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0
    """Initialize the class attritube to zero"""

    def __init__(self, id=None):
        """Initialize a new Base.

         Args:
           id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
