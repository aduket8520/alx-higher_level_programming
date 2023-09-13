#!/usr/bin/python3

def lookup(obj):
    """this function checks if the input is an object"""
    if not hasattr(obj, '__dict__'):
        return []

    """ Use dir() to get a list of attributes and methods"""
    """this shows what the function returns"""
    return dir(obj)
