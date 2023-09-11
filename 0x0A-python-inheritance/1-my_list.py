#!/usr/bin/python3

class MyList(list):
  """this defines the class named MyList"""
  
  def print_sorted(self):
    """this function """
    sorted_list = sorted(self)
    
    """function prints a sorted list"""
    print(sorted_list)
