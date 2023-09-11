#!/usr/bin/python3

class MyList(list):
  """this defines the class named MyList"""
  
  def print_sorted(self):
    """this function """
    sorted_list = sorted(self)
    print(sorted_list)
