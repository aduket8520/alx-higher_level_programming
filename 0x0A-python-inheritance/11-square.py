#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
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
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)  # Call the parent class constructor with equal width and height

    def __str__(self):
        return f"[Square] {self._Rectangle__width}"  # Accessing the private attribute of Rectangle
