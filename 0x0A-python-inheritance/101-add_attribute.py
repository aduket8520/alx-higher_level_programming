#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """define a function called add_attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
