#!/usr/bin/python3

class BaseGeometry:
    """implements a class"""
    def area(self):
        """this function defines the area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """implements a superclass Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """returns the area of the object"""
        return self.__width * self.__height

    def __str__(self):
        """formats the area """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """implements a subclass Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)  

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
