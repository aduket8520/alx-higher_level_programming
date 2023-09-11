#!/usr/bin/python3

class MyInt(int):
    """define a class named MyInt"""
    def __eq__(self, other):
        """a function that defines the equal operator"""
        return int(self) != other

    def __ne__(self, other):
        """function that defines the not equal operation"""
        return int(self) == other
