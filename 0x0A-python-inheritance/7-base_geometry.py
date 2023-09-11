#!/usr/bin/python3

class BaseGeometry:

  """implements the class BaseGeometry"""

  def area(self):
    """defines the area using the function"""
    raise Exception("araea() is not implemented")

  def integer_validator(self, name, value):
    if not isinstance(value, int):
      raise TypeError(f"{name} must be an integer")
    if value <= 0:
      raise ValueError(f"{name} must be greater than 0")
