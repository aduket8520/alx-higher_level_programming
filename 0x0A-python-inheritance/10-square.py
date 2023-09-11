#!/usr/bin/python3

class BaseGeometry:
    """defines a class BaseGeometry"""
    
    def area(self):
        """ define a function called area
            raises an exception if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define a program called integer_validator
        
            raises an exception message if not implemented
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """returns the area of the object"""
        return self.__width * self.__height

    def __str__(self):
        """formats the string elements"""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)  

    def __str__(self):
        return f"[Square] {self._Rectangle__width}"  